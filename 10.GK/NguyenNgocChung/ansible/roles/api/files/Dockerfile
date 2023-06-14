FROM python:3.9-alpine

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

CMD ["python","-u", "app.py"]