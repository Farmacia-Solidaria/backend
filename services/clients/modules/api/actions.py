from common.error.error import ActionError
from common.models.message import Message
from common.kafka.actions import ActionHandler
from common.kafka.guard import permissions_needed
from common.utils.validation import is_key_null

from modules.client.utils import is_cpf_valid
import modules.client.service as client_service

actioneer = ActionHandler()

@actioneer.register()
@permissions_needed(['gerente'])
async def register(message: Message):
    if (
        is_key_null(message.data['client'], 'first_name') or
        is_key_null(message.data['client'], 'cpf')
    ):
        raise ActionError(information="You need to provide a name and cpf")
    
    if (
        not is_cpf_valid(message.data['client']["cpf"])
    ):
        raise ActionError(information="You need to provide a valid cpf")
    
    message.data = await client_service.register_client(message.data)


@actioneer.default
async def default(message: Message):
    raise ActionError(
        information="Action not implemented",
        status=404
    )
