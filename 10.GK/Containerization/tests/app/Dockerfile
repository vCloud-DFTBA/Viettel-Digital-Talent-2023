FROM python:3.9-alpine

WORKDIR /app

COPY . .

RUN pip install "fastapi[all]" pymongo --no-cache-dir

CMD uvicorn main:app --reload --host 0.0.0.0 --port 8000