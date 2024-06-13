FROM python:3.9-alpine

ADD . /app
COPY . /app
WORKDIR /app

EXPOSE 9090
RUN pip install -r requirements.txt

CMD ["python","-u", "app.py"]

