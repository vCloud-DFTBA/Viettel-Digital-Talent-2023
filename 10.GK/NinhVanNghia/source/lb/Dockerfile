FROM nginx:1.22.0-alpine

ENV DEBIAN_FRONTEND=noninteractive

RUN apk update \
    && apk add --no-cache keepalived \
    && rm -rf /var/cache/apk/*

COPY nginx.conf /etc/nginx/conf.d/default.conf

COPY start.sh /start.sh
RUN chmod +x /start.sh

COPY keepalived-master.conf /etc/keepalived/keepalived-master.conf
COPY keepalived-backup.conf /etc/keepalived/keepalived-backup.conf

RUN chmod 644 /etc/keepalived/keepalived-master.conf
RUN chmod 644 /etc/keepalived/keepalived-backup.conf

CMD ["/bin/sh", "-c", "/start.sh"]
