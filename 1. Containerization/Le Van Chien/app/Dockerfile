FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
ENV FLASK_APP=app.py
COPY . .
CMD ["python", "app.py"]
