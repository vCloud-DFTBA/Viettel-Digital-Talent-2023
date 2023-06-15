FROM python:3.9

WORKDIR /src
COPY ./requirements.txt /src/requirements.txt
RUN pip install -r requirements.txt --no-cache-dir

EXPOSE 9000
CMD ["python","0.0.0.0:9000","./app.py"]