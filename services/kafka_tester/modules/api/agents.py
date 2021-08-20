import faust

from faust.types import StreamT
from modules.kafka_handler.app import faustApp

class Message(faust.Record, serializer='json'):
    action: str
    state: str
    data: dict

defaultInTopic = faustApp.topic("kafka_tester-income", value_type=Message)
defaultOutTopic = faustApp.topic("kafka_tester-outcome", value_type=Message)

@faustApp.agent(sink=[defaultOutTopic])
async def defaultAgent(messages: StreamT[Message]):
    print("Something:")
    async for event in messages:
        result = Message.objects.create(
            action=event.action,
            state=event.state,
            data=dict(event.data)
        )
        print(result, event)
        yield result.pk


@faustApp.agent(defaultInTopic, sink=[defaultAgent])
async def preProcess(messages):
    # Verify integrity here
     async for event in messages:
         print(event)
         yield event