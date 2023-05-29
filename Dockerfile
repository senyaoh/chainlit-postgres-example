FROM python:3.11.3-slim

WORKDIR /app
COPY ./requirements.txt ./requirements.txt

RUN pip install --requirement=requirements.txt

#RUN dbt init dbt-example

COPY . /app/