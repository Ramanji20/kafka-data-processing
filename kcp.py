import logging
from confluent_kafka import Consumer, Producer, KafkaError
import json

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configuration for Kafka consumer
consumer_conf = {
    'bootstrap.servers': 'localhost:29092',
    'group.id': 'my-consumer-group',
    'auto.offset.reset': 'earliest'
}

# Configuration for Kafka producer
producer_conf = {
    'bootstrap.servers': 'localhost:29092'
}

# Create Consumer and Producer instances
consumer = Consumer(consumer_conf)
producer = Producer(producer_conf)

# Subscribe to the 'user-login' topic
consumer.subscribe(['user-login'])

def process_message(msg):
    try:
        data = json.loads(msg.value().decode('utf-8'))
        # Perform data processing here (e.g., transform, aggregate, filter)
        processed_data = {
            "user_id": data.get("user_id", None),
            "device_type": data.get("device_type", "unknown"),
            "locale": data.get("locale", "unknown"),
            "processed_at": data.get("timestamp", None)
        }
        return json.dumps(processed_data).encode('utf-8')
    except Exception as e:
        logger.error(f"Error processing message: {e}")
        return None

def delivery_report(err, msg):
    if err is not None:
        logger.error(f"Message delivery failed: {err}")
    else:
        logger.info(f"Message delivered to {msg.topic()} [{msg.partition()}]")

try:
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                continue
            else:
                logger.error(msg.error())
                break

        processed_message = process_message(msg)
        if processed_message:
            producer.produce('processed-user-login', processed_message, callback=delivery_report)
            producer.flush()
finally:
    consumer.close()

