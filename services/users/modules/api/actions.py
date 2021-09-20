from common.error.error import ActionError
from common.error.handling import handleError
from common.models.message import Message
from common.kafka.actions import ActionHandler

actioneer = ActionHandler()

@actioneer.register
async def information(message: Message):
    try:
        message.data = "users is working correctly !!"
    except ActionError as ex:
        handleError(
            message,
            information=ex.args[0],
            where="login"
        )

@actioneer.register
async def teste(message: Message):
    try:
        message.data = "Teste message"
    except ActionError as ex:
        handleError(
            message,
            information=ex.args[0],
            where="login"
        )



@actioneer.default
async def default(message: Message):
    handleError(
        message,
        information="Action not implemented",
        where="users")
