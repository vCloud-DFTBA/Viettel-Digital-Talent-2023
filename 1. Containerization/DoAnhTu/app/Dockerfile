FROM python:3.9

ENV FLASK_APP=VDT
ENV FLASK_ENV=development

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt


COPY . .

EXPOSE 5000


CMD ["uwsgi", "--http", "127.0.0.1:8000", "--master", "-p", "4", "-w", "wsgi:app"]



