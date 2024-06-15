#!/bin/bash

# Container name
CONTAINER_NAME="my-container"
IMAGE_NAME="my-data-container"
LOCAL_DIR="$(pwd)/local_data"

# Create the local_data directory if it doesn't exist
mkdir -p $LOCAL_DIR

# Create the Dockerfile
cat > Dockerfile <<EOL
FROM alpine:latest
RUN apk add --no-cache bash
VOLUME /data
# Default command to keep the container running
CMD ["tail", "-f", "/dev/null"]
EOL

echo "Dockerfile created."

# Build the Docker image
docker build -t $IMAGE_NAME .

echo "Docker image built."

# Remove the existing container if it exists
if [ "$(docker ps -aq -f name=$CONTAINER_NAME)" ]; then
    docker stop $CONTAINER_NAME
    docker rm $CONTAINER_NAME
fi

# Run the container
docker run -d --name $CONTAINER_NAME -v $LOCAL_DIR:/data $IMAGE_NAME

echo "Docker container started."

# Write data to the volume
docker exec $CONTAINER_NAME sh -c 'echo "Hello, Docker Volumes!" > /data/hello.txt'

echo "Data written to volume."

# Read data from the volume
DATA=$(docker exec $CONTAINER_NAME cat /data/hello.txt)

echo "Data read from volume: $DATA"

# Stop the container
docker stop $CONTAINER_NAME

echo "Docker container stopped."

# Restart the container
docker start $CONTAINER_NAME

echo "Docker container restarted."

# Read data from the volume again after restart
RESTARTED_DATA=$(docker exec $CONTAINER_NAME cat /data/hello.txt)

echo "Data read from volume after restart: $RESTARTED_DATA"
