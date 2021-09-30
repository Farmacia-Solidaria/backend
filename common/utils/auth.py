from common.error.error import ActionError
import jwt 

from common.utils.information import get_public_key

def get_token_permissions(token):
    try:
        data = jwt.decode(token, get_public_key(), 'RS256')

        return data['permissions']
    except jwt.ExpiredSignatureError:
        raise ActionError(
            information="Token has expired",
            status=403
        )
    except:
        return []

