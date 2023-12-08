from confluent_kafka import Producer
import json
import time
import random
import string
import os

def generate_random_name():
    return ''.join(random.choice(string.ascii_letters) for _ in range(8))

def generate_random_age():
    return random.randint(18, 99)

def delivery_report(err, msg):
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

def produce_message(bootstrap_servers, topic, message):
    # Kafka producer configuration
    producer_conf = {
        'bootstrap.servers': bootstrap_servers,
        # You may add more configurations here
    }

    # Create a Kafka producer instance
    producer = Producer(producer_conf)

    # Produce a JSON-formatted message to the specified topic
    json_message = json.dumps(message)
    producer.produce(topic, key=None, value=json_message, callback=delivery_report)

    # Wait for any outstanding messages to be delivered and delivery reports to be received
    producer.flush()

if __name__ == '__main__':
    # Set your Kafka bootstrap servers and topic
    kafka_bootstrap_servers = os.getenv("KAFKA_BOOTSTRAP_SERVERS")
    kafka_topic = os.getenv("KAFKA_TOPIC")

    while True:
        # Generate random values for name and age
        random_name = generate_random_name()
        random_age = generate_random_age()

        # Message to be produced (JSON format)
        message_to_produce = {'name': random_name, 'age': random_age}

        # Produce the message
        produce_message(kafka_bootstrap_servers, kafka_topic, message_to_produce)

        # Sleep for a while before producing the next message (adjust as needed)
        time.sleep(1)
