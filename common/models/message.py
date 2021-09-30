import faust

class Message(faust.Record, serializer='json'):
    action: str
    data: dict
    id: str
    method: str
    error: bool = False
    token: str = ""