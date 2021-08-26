from kafka import KafkaConsumer

from common import settings

def build_kafka_consumer(topic):
    return KafkaConsumer(
        topic,
        bootstrap_servers=[settings.KAFKA_BROKER_URL],
        auto_offset_reset='earliest'
    )