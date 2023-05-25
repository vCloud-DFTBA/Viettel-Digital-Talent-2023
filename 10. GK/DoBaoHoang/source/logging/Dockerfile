FROM fluentd:v1.16.0-debian-1.0
COPY ./fluentd.conf /fluentd/etc/
USER root
RUN ["gem", "install", "elasticsearch", "--no-document", "--version", "< 8"]
RUN ["gem", "install", "fluent-plugin-elasticsearch", "--no-document", "--version", "5.2.2"]
USER fluent