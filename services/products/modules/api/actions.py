from common.error.handling import handleError
from common.models.message import Message
from common.kafka.actions import ActionHandler

actioneer = ActionHandler()

@actioneer.default
def default(message: Message):
    handleError(
        message,
        message="Action not implemented",
        where="products")
