FROM python:3.9

WORKDIR /app

EXPOSE 5000

ENV PYTHONDONTWRITEBYTECODE 1

COPY requirements.txt .
RUN python -m pip install -r requirements.txt

ADD . /app

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
