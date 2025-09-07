# Use Alpine Linux for smaller image size
FROM alpine:latest

# Install only essential networking tools
RUN apk add --no-cache \
    iputils \
    vim \
    net-tools \
    && rm -rf /var/cache/apk/*

# Create a non-root user for security
RUN adduser -D -s /bin/sh networkuser

# Switch to non-root user
USER networkuser

# Default command
CMD ["sleep", "infinity"]
