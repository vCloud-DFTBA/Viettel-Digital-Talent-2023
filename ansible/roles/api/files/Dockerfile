FROM python:3.9-alpine

WORKDIR /app
ADD . /app
COPY . /app

EXPOSE 9090
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python","-u", "app.py"]
