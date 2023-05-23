# Project giữa kỳ - Hoàng Quốc Doanh
## Phát triển một 3-tier web application đơn giản

 - Mã nguồn backend: [main.py](./web/app/main.py)
 - Mã nguồn frontend: [index.html](./web/nginx/index.html)
 - Mã nguồn unittest cho các chức năng API: [test_main.py](./web/tests/templates/test_main.py)

## Triển khai web application sử dụng các DevOps tools & practices

### 1. Containerization

- Dockerfile cho backend:
```Dockerfile
FROM python:3.9-alpine

WORKDIR /app

COPY . .

RUN pip install "fastapi[all]" pymongo --no-cache-dir

CMD uvicorn main:app --reload --host 0.0.0.0 --port 8000

```
- Dockerfile cho frontend:
```Dockerfile
FROM nginx:1.22.0-alpine

WORKDIR /usr/share/nginx/html

RUN rm -rf ./*

COPY ./* ./

ENTRYPOINT [ "nginx", "-g", "daemon off;" ]

```
