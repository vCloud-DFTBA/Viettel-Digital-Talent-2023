FROM nginx:1.22.0-alpine

COPY ./nginx.conf /etc/nginx/conf.d/default.conf

COPY ./frontend/index.html /usr/share/nginx/html
COPY ./frontend/update.html /usr/share/nginx/html
COPY ./frontend/create.html /usr/share/nginx/html

EXPOSE 80
