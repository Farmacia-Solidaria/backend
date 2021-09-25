from common.error.error import ActionError
import uuid
import json
import hashlib

from common.base import kafkaProducer
from common.models.message import Message
from common.kafka.builders import build_kafka_consumer, build_async_kafka_consumer


#region PUBLIC METHODS

async def async_send_and_wait_message(service, action, data, filter=False, suppress_errors=False) -> dict:
    key = str(uuid.uuid1())

    consumer = build_async_kafka_consumer(service+"-outcome", timeout_in_seconds=2)
    await consumer.start()
    
    send_message(service, action, data, key)

    async for event in consumer:
        value = json.loads(event.value.decode("utf-8"))
        if _treat_event(value, key, suppress_errors):
            await consumer.stop()
            
            if filter:
                value = _filter_value(value)

            return value

def send_and_wait_message(method, service, action, data, filter=False, suppress_errors=False) -> dict:
    key = str(uuid.uuid1())

    consumer = build_kafka_consumer(service+"-outcome", timeout_in_seconds=10)

    data = _treat_sensible_information(data)
    
    send_message(
        service=service, 
        action=action, 
        data=data, 
        method=method, 
        key=key
    )

    for event in consumer:
        value = json.loads(event.value.decode("utf-8"))
        if _treat_event(value, key, suppress_errors):
            consumer.close()
            if filter:
                value = _filter_value(value)
            return value

def send_message(service, action, data, method, key=""):
    finalKey = key if key != "" else str(uuid.uuid1())

    message = Message(
        action=action,
        method=method,
        data=data,
        id=finalKey,
    )
    try:
        _send_to_topic(service+"-income", finalKey, message.dumps())
        return finalKey
    
    except Exception as ex:
        print(ex)
        return False

#endregion

#region PRIVATE METHODS
def _send_to_topic(topic_name, key, value):
    print(topic_name, key, value)
    try:
        keyInBytes = bytes(key, encoding='utf-8')
        kafkaProducer.send(topic_name, key=keyInBytes, value=value)
        kafkaProducer.flush()
        return True
    except Exception as ex:
        raise ex

def _treat_event(value, key, suppress_errors):
    print("From recieving event: ", value)
    if "id" in value:
        if value['id'] == key:
            if value["error"] and not suppress_errors:
                raise ActionError(value["data"])

            return True
    return False

def _filter_value(value):
    return {
        "action": value["action"],
        "error": value["error"],
        "data": value["data"],
    }

def _treat_sensible_information(data):
    allow_list = ['password']

    for i in data:
        if i in allow_list:
            data[i] = hashlib.sha512(str(i).encode()).hexdigest()

    return data

#endregion