FROM python:3.9
WORKDIR /app
ENV FLASK_APP=api.py
ENV FLASK_RUN_HOST=0.0.0.0
COPY ./requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["python3", "-m", "flask", "run"]