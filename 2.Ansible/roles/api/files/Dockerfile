ARG DOCKER_BUILDKIT=1

FROM python:3.9-alpine as builder

WORKDIR /src
COPY requirements.txt /src
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .
EXPOSE 9090
CMD ["python","-u", "app.py"]
