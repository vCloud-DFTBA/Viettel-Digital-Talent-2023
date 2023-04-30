FROM python:3.9
WORKDIR /flask
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY ./server.py .
CMD ["python", "app.py]
