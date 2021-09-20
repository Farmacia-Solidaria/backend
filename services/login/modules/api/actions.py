from common.error.error import ActionError
from common.error.handling import handleError, checkError
from common.models.message import Message
from common.kafka.actions import ActionHandler
from common.kafka.send import async_send_and_wait_message, send_message

import asyncio


actioneer = ActionHandler()

@actioneer.register
async def auth(message: Message):
    message.data["JWToken"] = "fake-token-jwt"

@actioneer.register
async def self(message: Message):
    data = await async_send_and_wait_message(
        service="login", 
        action="auth", 
        data=message.data,
    )
    message.data = data['data']

@actioneer.register
async def whyAsync(message: Message):
    await asyncio.sleep(5)

@actioneer.register
async def teste123(message: Message):
    message.data["teste"] = "VALOR DE TESTE"

@actioneer.register
async def testForError(message: Message):

    try:
        print("1")
        await async_send_and_wait_message(
            service="products", 
            action="comeback", 
            data=message.data,
        )

        print("2")
        message = await async_send_and_wait_message(
            service="products", 
            action="345", 
            data=message.data,
        )

        print("3")
        send_message(
            service="login", 
            action="345", 
            data=message.data,
        )

        await asyncio.sleep(1)

        message.data["ok"] = "ended cycle"
        
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
        where="login")
