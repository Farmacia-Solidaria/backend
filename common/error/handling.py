from common.models.message import Message

def handleError(event: Message, message="", where=""):
    event.error = True
    event.data = {
        "message":message,
        "where":where
    }

def checkError(event: Message, where):

    if event.error:
        event.data['where'] = event.data['where'] + f"/{where}" if 'where' in event.data else where
        return True    
        
    return False