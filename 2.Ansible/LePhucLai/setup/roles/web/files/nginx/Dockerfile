FROM nginx:1.22.0-alpine

COPY ./app.conf /etc/nginx/conf.d/app.conf

EXPOSE 8000 443
CMD ["nginx", "-g", "daemon off;"]