from common.error.handling import handleError, checkError
from common.models.message import Message
from common.kafka.actions import ActionHandler
from common.kafka.send import send_and_wait_message


actioneer = ActionHandler()

@actioneer.register
def auth(message: Message):
    message.data["JWToken"] = "fake-token-jwt"

@actioneer.register
def testForError(message: Message):

    print("1")
    send_and_wait_message(
        service="products", 
        action="123", 
        data=message.data,
    )

    print("2")
    send_and_wait_message(
        service="products", 
        action="345", 
        data=message.data,
    )

    print("3")
    actioneer.run_action("123", message)

    print("4")
    actioneer.run_action("auth", message)

    message.data["ok"] = "ended cycle"

@actioneer.error_checking
def error(event: Message):
    return checkError(event, 'login')
        

@actioneer.default
def default(message: Message):
    handleError(
        message,
        message="Action not implemented",
        where="Login")
