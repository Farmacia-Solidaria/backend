from common.models.message import Message

def handleError(event: Message, information="", where=""):
    event.error = True
    event.data = {
        "information":information,
        "where":where
    }

def checkError(event: Message, where):
    if event.error:
        event.data['where'] = event.data['where'] + f"/{where}" if 'where' in event.data else where
        return True    
        
    return False