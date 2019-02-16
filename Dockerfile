FROM ubuntu:18.04

# Create a new project directory inside the container and copy the local project files into it.

WORKDIR /device-daemon
COPY ./device-daemon .

# Install project packages. Add any new ones to this list.

RUN apt-get update && apt-get install -y --no-install-recommends \
    apt-utils \
    openssh-server \
    sudo \
    vim \
    curl \
    net-tools \
    psmisc \
    iproute2 \
    inetutils-syslogd \
    ca-certificates \
    netcat-openbsd \
    less \
    lsof \
    systemd \
    nginx \
    expect \
    python3 \ 
    dropbear \
    ufw \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Expose the container's ports to requests from the host machine.

EXPOSE 22 80-9000

# Allow the nginx web server to run.

# RUN sudo ufw allow 'Nginx HTTP'

CMD [ "/bin/bash" ]