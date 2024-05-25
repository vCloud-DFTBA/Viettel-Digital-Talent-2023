FROM nginx:1.22.0-alpine

ENV FLASK_SERVER_ADDR_1=backend_1:9001
ENV FLASK_SERVER_ADDR_2=backend_2:9002

COPY ./nginx.conf /tmp/nginx.conf

CMD ["/bin/sh", "-c", "envsubst < /tmp/nginx.conf > /etc/nginx/conf.d/default.conf && nginx -g 'daemon off;'"]
