FROM python:3.9
RUN pip install django==3.0.3; 
RUN pip install djongo==1.3.1
RUN pip install pymongo==3.10.1 
RUN pip install uwsgi
COPY app /app
WORKDIR /app
ENTRYPOINT ["uwsgi"] 
CMD ["--http", "0.0.0.0:8000","--module","app.wsgi"]
EXPOSE 8000
