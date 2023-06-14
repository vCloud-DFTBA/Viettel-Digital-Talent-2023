FROM python:3.9-slim as builder

WORKDIR /app

ENV PIP_DEFAULT_TIMEOUT=100 \
    # Allow statements and log messages to immediately appear
    PYTHONUNBUFFERED=1 \
    # disable a pip version check to reduce run-time & log-spam
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    # cache is useless in docker image, so disable to reduce image size
    PIP_NO_CACHE_DIR=1

RUN set -ex \
    && apt-get update \
    && apt-get upgrade -y \
    && apt-get install binutils -y \
    && apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

COPY . .

RUN pyinstaller -w -F --noconfirm app.py && rm -rf /app/build


### deploy stage
FROM python:3.9-slim

EXPOSE 8000

RUN set -ex \
    && addgroup --system --gid 1001 appgroup \
    && adduser --system --uid 1001 --gid 1001 --no-create-home appuser \
    && apt-get update \
    && apt-get upgrade -y \
    && apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN chown -R appuser:appgroup /app

USER appuser

COPY --from=builder /app/data ./data
COPY --from=builder /app/dist/app .

CMD ["./app"]
