from common.error.error import ActionError
from common.models.message import Message
from common.kafka.actions import ActionHandler
from common.utils.validation import is_key_null
from common.kafka.guard import permissions_needed
from common.utils.functions import treat_token
from common.utils.auth import get_token_permissions

import modules.authorization.services as authorization_service

actioneer = ActionHandler()

@actioneer.register()
@permissions_needed(['atendente', 'gerente'])
async def get_self_permissions(message: Message):
    message.data = get_token_permissions(treat_token(message.token))

        

@actioneer.register('get')
async def auth(message: Message):
    if (
        is_key_null(message.data, 'username') or
        is_key_null(message.data, 'password')
    ):
        raise ActionError(information="You need to provide username and password")
    
    message.data = await authorization_service.auth(message.data)

   
@actioneer.register()
async def register(message: Message):
    if (
        is_key_null(message.data, 'username') or
        is_key_null(message.data, 'email') or
        is_key_null(message.data, 'password')
    ):
        raise ActionError(information="You need to provide username, password, email")
    
    message.data = await authorization_service.create_user(message.data)



@actioneer.register("get")
async def permissions(message: Message):
    if (is_key_null(message.data, 'username')):
        raise ActionError(information="You need to provide username and password")
    
    message.data = await authorization_service.get_permissions(message.data)


@actioneer.default
async def default(message: Message):
    raise ActionError(
        information="Action not implemented",
        status=404
    )
