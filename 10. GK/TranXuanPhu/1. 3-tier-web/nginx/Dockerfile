FROM nginx:1.22.0-alpine

RUN rm -f /etc/nginx/conf.d/default.conf /etc/nginx/conf.d/app.conf

COPY nginx.conf /etc/nginx/conf.d/

EXPOSE 80 443

CMD ["nginx", "-g", "daemon off;"]
