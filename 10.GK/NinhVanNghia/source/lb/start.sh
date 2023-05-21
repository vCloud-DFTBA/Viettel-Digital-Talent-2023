#!/bin/sh

/usr/sbin/keepalived -n -l -D -f /etc/keepalived/keepalived-${TYPE}.conf --dont-fork --log-console &

nginx -g "daemon off;"