FROM nginx:1.22.0-alpine

ENV FLASK_SERVER_ADDR=backend:5000

COPY ./nginx.conf /tmp/nginx.conf

CMD ["/bin/sh", "-c", "envsubst < /tmp/nginx.conf > /etc/nginx/conf.d/default.conf && nginx -g 'daemon off;'"]
