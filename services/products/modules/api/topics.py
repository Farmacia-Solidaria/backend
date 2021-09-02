from modules.kafka_handler.app import faustApp
from common.models.message import Message

defaultInTopic = faustApp.topic("products-income", value_type=Message)
defaultOutTopic = faustApp.topic("products-outcome", value_type=Message)