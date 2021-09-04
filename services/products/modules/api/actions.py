from common.error.error import ActionError
from common.error.handling import handleError
from common.models.message import Message
from common.kafka.actions import ActionHandler
from common.kafka.send import async_send_and_wait_message

actioneer = ActionHandler()

@actioneer.register
async def comeback(message: Message):
    try:
        await async_send_and_wait_message(
            service="login",
            action="i_expect_this_to_comeback",
            data=message.data
        )
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
        where="products")
