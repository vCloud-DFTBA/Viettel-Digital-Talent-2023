FROM python:3.9-alpine3.17
WORKDIR /web
COPY requirement.txt requirement.txt
RUN pip install --no-cache-dir -r requirement.txt && \
    rm requirement.txt
COPY . .
CMD ["python3", "-u", "app.py"]

