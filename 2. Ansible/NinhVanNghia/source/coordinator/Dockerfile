FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update \
    && apt install -y software-properties-common curl \
    && apt-add-repository ppa:ansible/ansible \
    && apt update \
    && apt install -y ansible \
    && apt remove -y software-properties-common \
    && apt autoremove -y \
    && apt clean -y \
    && rm -rf /var/lib/apt/lists/*

RUN VER=$( curl --silent "https://api.github.com/repos/tsl0922/ttyd/releases/latest"| grep '"tag_name"'|sed -E 's/.*"([^"]+)".*/\1/') \
    && curl -LO https://github.com/tsl0922/ttyd/releases/download/$VER/ttyd.x86_64 \
    && mv ttyd.* /usr/local/bin/ttyd \
    && chmod +x /usr/local/bin/ttyd

CMD ["ttyd", "bash"]
