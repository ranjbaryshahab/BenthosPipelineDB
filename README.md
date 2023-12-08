# BenthosPipelineDB

## Overview

BenthosPipelineDB is a project that utilizes Benthos, Kafka, and Postgres to process and store random user data. The project includes a data generator Python script that produces random data and publishes it to the `users` Kafka topic. Benthos consumes this data and inserts it into the `users` table in a PostgreSQL database.

## Project Structure

The project directory structure is organized as follows:
- /BenthosPipelineDB
  - /pipeline
    - benthos.yml
  - /postgres
    - /sql
        - create_table.sql
    - /data
  - /data-producer
    - message-producer.py
    - requirements.txt
    - Dockerfile 
  - config.env
  - docker-compose.yaml

## Setup

Before you begin, ensure you have the following installed:

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/BenthosPipelineDB.git
   cd BenthosPipelineDB
   ```
2. **Run Docker Compose:**
   ```bash
   docker-compose up -d
   ```
