FROM fluent/fluentd:v1.16-debian-1

USER root

RUN ["gem", "install", "elasticsearch", "--no-document", "--version", "< 8"]

RUN ["gem", "install", "fluent-plugin-elasticsearch", "--no-document", "--version", "5.2.2"]

USER fluent