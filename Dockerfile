FROM python:3.11-bullseye


ENV DockerHOME=/usr/src/app
RUN mkdir -p $DockerHOME
WORKDIR $DockerHOME  

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN pip install "gunicorn==20.0.4"

# Install libenchant and create the requirements folder.
RUN apt-get update -y \
    && apt-get install -y libenchant-2-dev postgresql-client \
    && mkdir -p /code/requirements

# Install python packages
RUN pip install --upgrade pip
RUN pip install numpy
RUN pip install pandas
RUN pip install "gunicorn==20.0.4"
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# Postgres Entrypoint
COPY entrypoint.sh /usr/src/app/entrypoint.sh
COPY entrypoint.prod.sh /usr/src/app/entrypoint.prod.sh