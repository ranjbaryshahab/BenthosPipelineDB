# Using Benthos: A Practical Guide for Kafka and PostgreSQL Integration

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

1- Navigate to the project directory:

```bash
cd /path/to/BenthosPipelineDB
```


2- Start the project using Docker Compose:

```bash
docker-compose up -d
```


3- Monitor logs to ensure everything is running smoothly:

```bash
docker-compose logs -f
```

4- Kafka Console Consumer
If you want to observe the data flowing through the users topic in real time, you can use the Kafka console consumer. Open your terminal and run the following command:


```bash
docker-compose exec kafka kafka-console-consumer.sh --topic users --from-beginning --bootstrap-server kafka:9092
```


5- Connecting to PostgreSQL
To inspect the data in the PostgreSQL database, you can use a PostgreSQL client. Assuming you have PostgreSQL installed locally, you can connect using the following command:


```bash
psql -h localhost -p 5432 -U postgres -d postgres
```


6- Now, let's run a simple query to fetch the first 10 records from the users' table:


```bash
SELECT * FROM users LIMIT 10;
```

## Project Documentation

- [BenthosPipelineDB Article](https://dev.to/ranjbaryshahab/using-benthos-a-practical-guide-for-kafka-and-postgresql-integration-2dln) - Explanation of the BenthosPipelineDB project and how it works.
