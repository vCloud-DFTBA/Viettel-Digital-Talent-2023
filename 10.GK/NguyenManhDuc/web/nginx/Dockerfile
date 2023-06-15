FROM nginx:1.23.4-alpine-slim

RUN rm /etc/nginx/conf.d/default.conf

COPY nginx.conf /etc/nginx/conf.d/
# COPY ./templates /etc/nginx/templates/