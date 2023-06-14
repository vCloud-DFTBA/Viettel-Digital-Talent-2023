FROM mongo:5.0.17

# Set the container name
# ENV container_name mongo_test_1

# Expose port 27017
EXPOSE 27017

# Set up a health check
HEALTHCHECK --interval=5s \
            --timeout=5s \
            CMD mongo --eval "print(\"MongoDB is up and running\")" || exit 1

# Set up the command to run the container
CMD ["mongod", "--bind_ip_all"]