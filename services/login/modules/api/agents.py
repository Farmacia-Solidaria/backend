from faust.types import StreamT
from common.models.message import Message

from .actions import actioneer
from .topics import defaultInTopic, defaultOutTopic
from modules.kafka_handler.app import faustApp



@faustApp.agent(defaultInTopic, sink=[defaultOutTopic])
async def defaultAgent(messages: StreamT[Message]):
    async for event in messages:
        event.state = "Done"
        
        actioneer.run_action(event.action, event.data)
        
        yield event