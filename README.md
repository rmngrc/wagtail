# CMS Experiment

First, create a virtual environment like this:

```
cd PROJECT_DIR

python3 -m venv .env
```

Then, if using Visual Studio Code:

- Install Python extension.
- Then the press `Cmd` + `Shift` + `P` and select `Select python interpreter`.
- Select the one from the virtual environment you just created.

This done, each time you open up the terminal within Visual Studio Code, it will source the environment for you. 

Now it's time to install dependencies to get cool things like autocomplete, linting and stuff:

```
pip install -r requirements.txt
```


Last bit:

```
docker-compose up
```

And you're done!