#!/usr/bin/env bash

set -e

LOCALES_LIST=("fr" "uk")

command -v docker-compose >/dev/null 2>&1 || {
	echo >&2 "docker-compose is required but not installed."
	echo >&2 "See https://docs.docker.com/compose/install/"
	echo >&2 "Aborting."
	exit 1
}

command -v python3 >/dev/null 2>&1 || {
	echo >&2 "python3 is required but not installed."
	echo >&2 "If you are on mac, you can just brew install python"
	echo >&2 "Aborting."
	exit 1
}

function success_msg() {
  echo -e >&2 "\033[32m$1\033[0;39m"
}

function warning_msg() {
  echo -e >&2 "\033[33m$1\033[0;39m"
}

function error_msg() {
  echo -e >&2 "\033[31mERROR: $1 \033[0;39m"
}

function error_msg_and_exit() {
  echo -e >&2 "\033[31mERROR: $1 \033[0;39m"
  exit 1
}

function usage() {
    if [ -n "$1" ]; then
        error_msg "$1"
        echo ""
    fi

    echo "$0 <commands>"
    echo ""
    echo "General commands:"
    echo "   help                          Prints this message"
    echo ""
    echo "Build commands:"
    echo "   setup                         Runs the initial setup. This may take a while."
    echo "   run                           Runs the project for all locales."
    echo ""
    echo "Development commands:"
    echo "   py_run <command> [locale]     Runs the given command for the specified locale."
    echo "                                 If no locale provided, it will run the command for all of them."
    exit 1
}

function help() {
    usage
}

# Gets the full path to the project directory.
function project_dir() {
  echo "$(git rev-parse --show-toplevel)"
}

# Sets up your environment for local development.
function setup() {
	[[ -d ".env" ]] || python3 -m venv .env
	source ".env/bin/activate"
	pip install -r requirements.txt
}

# Runs the project.
function run() {
    docker-compose up
}

# Running the provided command within all containers
# To see all available commands, use `help`
function py_run() {
    if [[ $2 == "" ]]; then
        error_msg_and_exit "No command provided. Aborting."
    fi

    if [[ $3 == "" ]]; then
        LOCALES=("${LOCALES_LIST[@]}")
    else
        LOCALES=("$3")
    fi

    for LOCALE in "${LOCALES[@]}"; do
        docker-compose run web-${LOCALE} python manage.py $2
    done
}


cd `project_dir`
exec_command=$1

if [[ $(type -t ${exec_command} 2>/dev/null) == function ]]; then
  echo "Running command: ${exec_command}"
  ${exec_command} "$@"
  shift
else
  usage "Command ${exec_command} does not exist"
fi
