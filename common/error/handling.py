from common.models.message import Message

def handleError(event: Message, information="", where="", status=400):
    event.error = True
    event.data = {
        "information": information,
        "where": where,
        "status": status,
    }

def checkError(event: Message, where):
    if event.error:
        event.data['where'] = event.data['where'] + f"/{where}" if 'where' in event.data else where
        return True    
        
    return False