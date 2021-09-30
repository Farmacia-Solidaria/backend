import functools

import jwt

from common.utils.auth import get_token_permissions
from common.utils.functions import treat_token
from common.models.message import Message
from common.error.error import ActionError

def permissions_needed(permissions_needed: 'list[str]') -> 'function':

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):

            permissions = []

            if type(args[0]) is Message:
                message: Message = args[0]
                permissions = get_token_permissions(treat_token(message.token))

            if len(set(permissions_needed).intersection(permissions)) > 0 or 'admin' in permissions:
                return func(*args, **kwargs)

            raise ActionError(
                information="Permission denied",
                status=401
            )

        
        return wrapper
        
    return decorator
