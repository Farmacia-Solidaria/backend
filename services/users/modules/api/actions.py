from common.error.error import ActionError
from common.models.message import Message
from common.kafka.actions import ActionHandler
from common.error.handling import handleError
from common.utils.validation import is_key_null

import modules.authorization.services as authorization_service

actioneer = ActionHandler()


@actioneer.register
async def auth(message: Message):
    try:
        if (
            is_key_null(message.data, 'username') or
            is_key_null(message.data, 'password')
        ):
            raise ActionError("You need to provide username and password")
        
        message.data["token"] = "Fake Token"

    except ActionError as ex:
        handleError(
            message,
            information=ex.args[0],
            where="login"
        )

@actioneer.register
async def register(message: Message):
    try:
        if (
            is_key_null(message.data, 'username') or
            is_key_null(message.data, 'email') or
            is_key_null(message.data, 'password')
        ):
            raise ActionError("You need to provide username and password")
        
        message.data = await authorization_service.create_user(message.data)

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
