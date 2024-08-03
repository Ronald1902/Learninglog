FROM python:3.9.16-buster

# set work directory
WORKDIR /var/app

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /var/app
RUN pip install -r requirements.txt
