# Use the Alpine base image
FROM alpine

# Install the curl package
RUN apk add --no-cache curl

# Add the config.txt file to a suitable location in the container
COPY config.txt /app/config.txt

# Define the command to run when the container starts
CMD ["echo", "Container is ready!"]
