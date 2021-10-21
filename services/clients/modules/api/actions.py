from common.error.error import ActionError
from common.models.message import Message
from common.kafka.actions import ActionHandler
from common.kafka.guard import permissions_needed
from common.utils.functions import treat_token
from common.utils.auth import get_token_permissions

actioneer = ActionHandler()

@actioneer.register()
async def information(message: Message):
    message.data = "clients is working correctly !!"

@actioneer.register()
@permissions_needed(['gerente'])
async def private_information(message: Message):
    message.data = "clients is working with permissions !!"


@actioneer.default
async def default(message: Message):
    raise ActionError(
        information="Action not implemented",
        status=404
    )
