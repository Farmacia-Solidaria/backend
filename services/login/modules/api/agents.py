from common.error.handling import checkError
from faust.types import StreamT
from common.models.message import Message

from modules.api.actions import actioneer
from modules.api.topics import defaultInTopic, defaultOutTopic
from modules.kafka_handler.app import faustApp

@faustApp.agent(defaultInTopic, sink=[defaultOutTopic], concurrency=20)
async def defaultAgent(messages: StreamT[Message]):
    async for event in messages:
        if checkError(event, 'login'):
            yield event
        
        action = actioneer.get_action(event.action)
        await action(event)
        
        yield event

@faustApp.agent(defaultInTopic, sink=[defaultOutTopic], concurrency=20)
async def defaultAgent2(messages: StreamT[Message]):
    async for event in messages:
        if checkError(event, 'login'):
            yield event
        
        action = actioneer.get_action(event.action)
        await action(event)
        
        yield event