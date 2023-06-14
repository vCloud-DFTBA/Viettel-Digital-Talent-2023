FROM nginx:1.22.0-alpine
COPY ./nginx.conf  /etc/nginx/conf.d/default.conf
COPY ./static /etc/static
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]