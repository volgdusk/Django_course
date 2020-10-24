FROM python:3.9-alpine
LABEL mainteiner = "Anggelo Novack"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app/ /app

#creates a user for only running the aplication
RUN adduser -D user
USER user
