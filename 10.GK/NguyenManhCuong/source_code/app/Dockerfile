FROM python:3.9-alpine3.17
WORKDIR /app
EXPOSE 5000
RUN pip install --no-cache-dir -U pip

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt && \
    rm requirements.txt
COPY . .
CMD [ "python3", "app.py" ]
