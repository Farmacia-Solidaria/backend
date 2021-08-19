from modules.kafka_handler.app import kafkaProducer

def publish_message(topic_name, key, value):
    try:
        keyInBytes = bytes(key, encoding='utf-8')
        valueInBytes = bytes(value, encoding='utf-8')
        kafkaProducer.send(topic_name, key=keyInBytes, value=valueInBytes)
        kafkaProducer.flush()
        return True
    except Exception as ex:
        return False