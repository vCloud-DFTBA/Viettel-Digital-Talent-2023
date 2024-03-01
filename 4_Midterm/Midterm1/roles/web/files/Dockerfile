FROM nginx:1.22.0-alpine

COPY ./nginx.conf /etc/nginx/conf.d/default.conf

COPY ./templates/ /usr/share/nginx/html

EXPOSE 80    