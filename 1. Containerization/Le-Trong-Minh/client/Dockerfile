FROM nginx:1.22.0-alpine

WORKDIR /usr/share/nginx/html

COPY ./* ./

ENTRYPOINT [ "nginx", "-g", "daemon off;" ]