import faust

class Message(faust.Record, serializer='json'):
    action: str
    state: str
    data: dict
    id: str