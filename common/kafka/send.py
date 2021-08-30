import uuid
import json
import os

from common.base import kafkaProducer
from common.models.message import Message
from common.kafka.builders import build_kafka_consumer


#region PUBLIC METHODS

def send_and_wait_message(service, action, data, filter=False) -> dict:
    key = str(uuid.uuid1())

    consumer = build_kafka_consumer(service+"-outcome")

    send_message(service, action, data, key)

    for event in consumer:
        value = json.loads(event.value.decode("utf-8"))
        if "id" in value:
            if value['id'] == key:
                consumer.close()

                if filter:
                    value = {
                        "action": value["action"],
                        "error": value["error"],
                        "data": value["data"],
                    }

                return value

def send_message(service, action, data, key=""):
    finalKey = key if key != "" else str(uuid.uuid1())

    message = Message(
        action=action,
        data=data,
        id=finalKey
    )
    try:
        _send_to_topic(service+"-income", finalKey, message.dumps())
        return finalKey
    
    except Exception as ex:
        print(ex)
        return False

#endregion

#region HELPER METHODS
def _send_to_topic(topic_name, key, value):
    print(topic_name, key, value)
    try:
        keyInBytes = bytes(key, encoding='utf-8')
        kafkaProducer.send(topic_name, key=keyInBytes, value=value)
        kafkaProducer.flush()
        return True
    except Exception as ex:
        raise ex
#endregion