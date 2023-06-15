FROM nginx:1.22.0-alpine
    
WORKDIR /src
    
RUN rm -rf ./*
    
EXPOSE 800

ENTRYPOINT [ "nginx", "-g", "daemon off;" ]
