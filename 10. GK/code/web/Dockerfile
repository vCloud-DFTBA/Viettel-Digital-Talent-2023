FROM nginx:latest


RUN rm /etc/nginx/conf.d/default.conf

COPY nginx.conf /etc/nginx/conf.d/default.conf

COPY /web/ /usr/share/nginx/html