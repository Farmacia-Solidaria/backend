import faust

class Message(faust.Record, serializer='json'):
    action: str
    data: dict
    id: str
    error: bool = False