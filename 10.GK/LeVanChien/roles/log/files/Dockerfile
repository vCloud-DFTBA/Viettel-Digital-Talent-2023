FROM fluent/fluentd:v1.14-1
USER root
RUN fluent-gem install fluent-plugin-elasticsearch

COPY ./fluent.conf /fluentd/etc/fluent.conf
WORKDIR /nginx
EXPOSE 24224

# Start Fluentd
CMD ["fluentd", "-c", "/fluentd/etc/fluent.conf"]