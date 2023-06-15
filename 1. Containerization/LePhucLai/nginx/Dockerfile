FROM nginx:1.22.0-alpine

COPY conf.d/app.conf /etc/nginx/conf.d/app.conf

EXPOSE 8000 433
CMD ["nginx", "-g", "daemon off;"]