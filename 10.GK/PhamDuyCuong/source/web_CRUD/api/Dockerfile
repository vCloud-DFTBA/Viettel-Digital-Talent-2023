# syntax = docker/dockerfile:experimental
FROM python:3.9-alpine3.17

ENV DB_HOSTNAME=77.234.193.84
ENV DB_USERNAME=admin
ENV DB_PASSWORD=vdt23
ENV DATABASE_NAME=VDT2023


WORKDIR /src

COPY requirements.txt .
RUN pip3 install -r requirements.txt


COPY . .
ENTRYPOINT ["python3", "run.py"]

