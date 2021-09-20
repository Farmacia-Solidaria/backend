from common.error.handling import handleError
from common.models.message import Message
from common.kafka.actions import ActionHandler


actioneer = ActionHandler()

@actioneer.register
async def auth(message: Message):
    message.data["JWToken"] = "fake-token-jwt"

@actioneer.default
async def default(message: Message):
    handleError(
        message,
        information="Action not implemented",
        where="login")
