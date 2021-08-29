from common.error.handling import handleError
from common.models.message import Message
from common.kafka.actions import ActionHandler


actioneer = ActionHandler()

@actioneer.register
def auth(message: Message):
    message.data["JWToken"] = "fake-token-jwt"

@actioneer.default
def default(message: Message):
    handleError(
        message,
        message="Action not implemented",
        where="Login")
