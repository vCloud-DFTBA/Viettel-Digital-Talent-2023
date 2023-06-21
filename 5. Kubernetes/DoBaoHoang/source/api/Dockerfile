FROM python:3.9.16-alpine3.17

RUN pip install --upgrade pip && \
    addgroup -S webapp && \
    adduser -D --ingroup webapp webapp 

USER webapp

WORKDIR /var/www/
COPY ./requirements.txt /var/www/requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["/bin/sh", "-c", "python3 init.py;python3 -m gunicorn -w 4 -b 0.0.0.0:1234 app"]