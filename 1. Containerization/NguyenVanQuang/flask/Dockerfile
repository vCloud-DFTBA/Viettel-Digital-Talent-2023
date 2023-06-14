FROM python:3.9-alpine3.17

WORKDIR /src

COPY requirement.txt .
RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install -r requirement.txt

COPY . .
ENTRYPOINT ["python3", "app.py"]