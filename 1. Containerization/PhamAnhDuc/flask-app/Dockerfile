FROM python:3.9-slim-buster

WORKDIR /app

COPY ./requirement_version.txt .

RUN pip install --no-cache-dir -r requirement_version.txt

COPY . .

EXPOSE 5000

CMD ["python", "/app/app.py"]