from common.kafka.actions import ActionHandler

actioneer = ActionHandler()

@actioneer.register
def login(data):
    data["JWToken"] = "fake-token-jwt"
    return "logged in"