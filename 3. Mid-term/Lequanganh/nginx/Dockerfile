FROM nginx:stable-alpine3.17-slim

# Set the working directory to /app
WORKDIR /app

# Copy the Nginx configuration file to the container
COPY ./nginx1.conf /etc/nginx/conf.d/default.conf

# Copy the static files for the Flask app to the container
COPY ./static /app/static

# Expose port 80
EXPOSE 80

# Set the container name
ENV container_name nginx_test_1

# Set up dependencies
RUN apk update && \
    apk add --no-cache bash

# Set up a health check
HEALTHCHECK --interval=5s \
            --timeout=5s \
            CMD curl --fail http://localhost:80 || exit 1

# Set up the command to run the container
CMD ["nginx", "-g", "daemon off;"]