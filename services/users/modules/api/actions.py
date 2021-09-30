from common.error.error import ActionError
from common.models.message import Message
from common.kafka.actions import ActionHandler
from common.error.handling import handleError
from common.utils.validation import is_key_null
from common.kafka.guard import permissions_needed

import modules.authorization.services as authorization_service

actioneer = ActionHandler()

@actioneer.register()
@permissions_needed('namorada')
async def get_self_permissions(message: Message):
    try:
        if (
            is_key_null(message.data, 'username') or
            is_key_null(message.data, 'password')
        ):
            raise ActionError(information="You need to provide username and password")
        
        message.data = await authorization_service.auth(message.data)

    except ActionError as ex:
        handleError(
            message,
            information=ex.information,
            status=ex.status,
            where=ex.where
        )

@actioneer.register()
async def auth(message: Message):
    try:
        if (
            is_key_null(message.data, 'username') or
            is_key_null(message.data, 'password')
        ):
            raise ActionError(information="You need to provide username and password")
        
        message.data = await authorization_service.auth(message.data)

    except ActionError as ex:
        handleError(
            message,
            information=ex.information,
            status=ex.status,
            where=ex.where
        )

@actioneer.register()
async def register(message: Message):
    try:
        if (
            is_key_null(message.data, 'username') or
            is_key_null(message.data, 'email') or
            is_key_null(message.data, 'password')
        ):
            raise ActionError(information="You need to provide username, password, email")
        
        message.data = await authorization_service.create_user(message.data)

    except ActionError as ex:
        handleError(
            message,
            information=ex.information,
            status=ex.status,
            where=ex.where
        )

@actioneer.register("get")
async def permissions(message: Message):
    try:
        if (is_key_null(message.data, 'username')):
            raise ActionError(information="You need to provide username and password")
        
        message.data = await authorization_service.get_permissions(message.data)

    except ActionError as ex:
        handleError(
            message,
            information=ex.information,
            status=ex.status,
            where=ex.where
        )

@actioneer.default
async def default(message: Message):
    handleError(
        message,
        information="Action not implemented",
        where="users",
        status=404
    )
