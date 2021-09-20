from modules.kafka_handler.app import faustApp
from common.models.message import Message

defaultInTopic = faustApp.topic("users-income", value_type=Message)
defaultOutTopic = faustApp.topic("users-outcome", value_type=Message)