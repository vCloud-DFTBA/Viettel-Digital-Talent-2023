FROM python:3.9-alpine

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt --no-cache-dir

CMD gunicorn --bind 0.0.0.0:5000 wsgi:app