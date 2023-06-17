FROM python:3.11
RUN  pip install django==3.0.3 && pip install djongo==1.3.1 && pip install  pymongo==3.10.1 && pip install uwsgi && pip install requests
COPY app /app
WORKDIR /app
ENTRYPOINT ["uwsgi"] 
CMD ["--http", "0.0.0.0:8000","--module","app.wsgi"]
EXPOSE 8000
