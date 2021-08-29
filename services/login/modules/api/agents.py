from common.error.handling import checkError
from faust.types import StreamT
from common.models.message import Message

from modules.api.actions import actioneer
from modules.api.topics import defaultInTopic, defaultOutTopic
from modules.kafka_handler.app import faustApp

@faustApp.agent(defaultInTopic, sink=[defaultOutTopic])
async def defaultAgent(messages: StreamT[Message]):
    async for event in messages:
        if checkError(event, 'login'):
            yield event
        
        actioneer.run_action(event.action, event)
        
        yield event