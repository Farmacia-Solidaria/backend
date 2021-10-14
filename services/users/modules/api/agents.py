from common.error.error import ActionError
from faust.types import StreamT

from common.error.handling import handleError, checkError
from common.models.message import Message
from common.utils.consts import DEBUG

from modules.api.actions import actioneer
from modules.api.topics import defaultInTopic, defaultOutTopic
from modules.kafka_handler.app import faustApp

@faustApp.agent(defaultInTopic, sink=[defaultOutTopic], concurrency=10)
async def defaultAgent(messages: StreamT[Message]):
    async for event in messages:
        try:
            if checkError(event, 'users'):
                yield event
            
            action = actioneer.get_action(event.method, event.action)
            await action(event)
            
        except ActionError as ex:
            handleError(
                event,
                information=ex.information,
                status=ex.status,
                where=ex.where
            )
        
        except Exception as ex:
            handleError(
                event,
                information=str(ex) if DEBUG else "An unknow error has occured",
                status=500,
                where="users"
            )
            
        finally:
            yield event
        