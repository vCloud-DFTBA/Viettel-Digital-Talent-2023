FROM python:3.8-slim

WORKDIR /usr/src/app

COPY requirements.txt requirements.txt

RUN apt update && \
    apt install -y gcc libmariadb-dev-compat libmariadb-dev && \
    pip3 install -r requirements.txt --no-cache-dir && \
    rm -f flask_requirements.txt

COPY . .
EXPOSE 5000

CMD [ "python3" ,"__init__.py" ]