FROM python:3.9-alpine3.17

WORKDIR /usr/src/app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt --no-cache-dir && \
    rm -f flask_requirements.txt

COPY . .
EXPOSE 5000

CMD [ "python3" ,"app.py" ]