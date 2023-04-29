FROM python:3.9-alpine3.17

WORKDIR /web

COPY requirement.txt requirement.txt
RUN apk add --no-cache gcc musl-dev libffi-dev openssl-dev && \
    pip install --no-cache-dir -r requirement.txt && \
    apk del gcc musl-dev libffi-dev openssl-dev

COPY . .

CMD ["python", "app.py"]

