FROM python:3.9.16-alpine3.18

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt ; \
    rm -f requirements.txt

COPY . .

CMD ["python3", "init.py"]
