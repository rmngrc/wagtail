FROM python:3.7

# Set environment varibles
ENV PYTHONUNBUFFERED 1
ENV DJANGO_ENV dev

# Install any needed packages specified in requirements.txt
COPY ./requirements.txt /code/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /code/requirements.txt
RUN pip install gunicorn

# Copy the current directory contents into the container at /code/
# COPY . /code/

# Set the working directory to /code/
WORKDIR /code/

# RUN python manage.py migrate

RUN useradd wagtail
RUN chown -R wagtail /code
USER wagtail
