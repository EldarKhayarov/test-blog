FROM python:3.6-alpine

ENV PYTHONUNBUFFERED 1
WORKDIR /opt/server
COPY ./src .
COPY requirements.txt requirements.txt
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install -r requirements.txt
