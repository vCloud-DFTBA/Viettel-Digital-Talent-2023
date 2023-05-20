# syntax = docker/dockerfile:experimental
FROM python:3.9-alpine3.17

WORKDIR /src

COPY requirements.txt .
RUN pip3 install -r requirements.txt


COPY . .
ENTRYPOINT ["python3", "run.py"]

