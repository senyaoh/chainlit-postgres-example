FROM python:3.11.3-slim

WORKDIR /app
COPY ./requirements.txt ./requirements.txt

RUN pip install --requirement=requirements.txt

COPY . /app/