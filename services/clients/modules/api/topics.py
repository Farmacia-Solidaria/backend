from modules.kafka_handler.app import faustApp
from common.models.message import Message

defaultInTopic = faustApp.topic("clients-income", value_type=Message)
defaultOutTopic = faustApp.topic("clients-outcome", value_type=Message)