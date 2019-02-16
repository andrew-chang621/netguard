FROM ubuntu:18.04

# Create a new project directory inside the container and copy the local project files into it.

WORKDIR /device-daemon
COPY ./ ./

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

EXPOSE 22 80 3000 8000

# Allow the nginx web server to run.

# RUN sudo ufw enable
# RUN ssudo ufw status verbose
# RUN sudo ufw logging on
# RUN sudo ufw allow 'Nginx HTTP'

# CMD [ "/bin/bash" ]

# ! TODO
# * 1. script to set up ufw
# * 2. find where logs are
# * 3. automate process with docker build
# * 4.

ENTRYPOINT ["tail", "-f", "/dev/null"]`