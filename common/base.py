import uuid
import json

from kafka import KafkaConsumer, KafkaProducer

from common import settings

kafkaProducer = KafkaProducer(bootstrap_servers=[settings.KAFKA_BROKER_URL]) 