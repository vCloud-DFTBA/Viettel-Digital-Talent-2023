FROM python:3.9-alpine

WORKDIR /app
COPY . /app

EXPOSE 9090

RUN pip install -r requirements.txt

CMD ["python","-u", "app.py"]
