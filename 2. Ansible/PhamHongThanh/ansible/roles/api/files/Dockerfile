FROM python:3.10.6-alpine
WORKDIR /app
RUN pip install --no-cache-dir --upgrade pip
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY ./app.py .
CMD ["python", "app.py"]
