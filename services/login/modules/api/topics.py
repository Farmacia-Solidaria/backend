from modules.kafka_handler.app import faustApp
from common.models.message import Message

defaultInTopic = faustApp.topic("login-income", value_type=Message, key_type=str)
defaultOutTopic = faustApp.topic("login-outcome", value_type=Message, key_type=str)