FROM python:3.9-alpine3.17

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt && \
    rm -f requirements.txt

COPY . .

CMD ["python3", "app.py"]
