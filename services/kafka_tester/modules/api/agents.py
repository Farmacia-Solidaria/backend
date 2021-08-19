import faust

from faust.types import StreamT
from kafka_handler.app import faustApp

class Message(faust.Record, serializer='json'):
    action: str
    state: str
    data: dict

defaultInTopic = faust.Topic("kafka_tester-income", value_type=Message)
defaultOutTopic = faust.Topic("kafka_tester-outcome", value_type=Message)

@faustApp.Agent(defaultInTopic, sink=[defaultOutTopic])
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


@faustApp.agent(sink=[defaultAgent])
async def preProcess(messages):
    # Verify integrity here
     async for event in messages:
         print(event)
         yield event