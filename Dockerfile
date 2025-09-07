FROM ubuntu:latest

RUN apt-get update && apt-get install -y iputils-ping vim net-tools \
    && rm -rf /var/lib/apt/lists/*

CMD ["sleep", "infinity"]
