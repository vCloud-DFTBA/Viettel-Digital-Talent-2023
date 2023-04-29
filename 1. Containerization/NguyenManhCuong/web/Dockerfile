# stage 1
FROM python:3.9-alpine3.17
WORKDIR /init
COPY requirement-init.txt requirement.txt
RUN pip install --no-cache-dir -r requirement.txt && \
    rm requirement.txt
COPY init.py init.py
CMD ["python3", "init.py"]

# stage 2
FROM python:3.9-alpine3.17
WORKDIR /web
COPY requirement.txt requirement.txt
RUN pip install --no-cache-dir -r requirement.txt && \
    rm requirement.txt
COPY . .
CMD ["python3", "app.py"]
