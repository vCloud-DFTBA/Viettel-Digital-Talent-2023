FROM python:3.9-alpine3.17

WORKDIR /src

COPY requirements.txt .
RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install -r requirements.txt

COPY . .
ENTRYPOINT ["python3", "server.py"]

