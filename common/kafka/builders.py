from uuid import uuid1

from kafka import KafkaConsumer
from aiokafka import AIOKafkaConsumer

from common import settings

import asyncio

loop = asyncio.get_event_loop()

def build_kafka_consumer(topic, timeout_in_seconds=15):
    return KafkaConsumer(
        topic,
        bootstrap_servers=[settings.KAFKA_BROKER_URL],
        auto_offset_reset='earliest',
        consumer_timeout_ms=float(1000*timeout_in_seconds)

    )

def build_async_kafka_consumer(topic, timeout_in_seconds=15):
    return AIOKafkaConsumer(
        topic,
        loop=loop,
        bootstrap_servers=[settings.KAFKA_BROKER_URL],
        auto_offset_reset='earliest',
        consumer_timeout_ms=float(1000*timeout_in_seconds)

    )