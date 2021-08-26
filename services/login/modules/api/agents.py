import faust

from faust.types import StreamT

from modules.api.topics import defaultInTopic, defaultOutTopic
from modules.kafka_handler.app import faustApp
from common.models.message import Message


@faustApp.agent(defaultInTopic, sink=[defaultOutTopic])
async def defaultAgent(messages: StreamT[Message]):
    async for event in messages:
        event.state = "Done"
        event.data["JWToken"] = "fake-token-jwt"
        print(event)
        yield event