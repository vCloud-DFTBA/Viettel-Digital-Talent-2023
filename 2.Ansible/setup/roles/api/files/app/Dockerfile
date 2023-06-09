FROM python:3.9

WORKDIR /var/www/

ADD . /var/www/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD gunicorn -w 4 -b 0.0.0.0:5000 app:application
