from modules.kafka_handler.app import faustApp
from common.models.message import Message

defaultInTopic = faustApp.topic("login-income", value_type=Message)
defaultOutTopic = faustApp.topic("login-outcome", value_type=Message)