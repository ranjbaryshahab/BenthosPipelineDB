# Use an official Python runtime as a parent image
FROM python:3.8-alpine

# Install build dependencies
RUN apk add --no-cache \
    build-base \
    openssl-dev \
    libffi-dev \
    librdkafka-dev

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run script.py when the container launches
CMD ["python", "./message-producer.py"]
