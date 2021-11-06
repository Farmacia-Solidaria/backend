from base64 import b64decode
from uuid import uuid1

from asgiref.sync import sync_to_async
from django.core.files.base import ContentFile

from modules.data.models import Client, ClientDetails, Address

from common.utils.validation import is_key_null
from common.error.error import ActionError
from common.utils.functions import get_or_none

@sync_to_async
def register_client(data):
    if get_or_none(Client, cpf=data['client']['cpf']) is not None:
        raise ActionError(
            information="Cpf is duplicated",
            status=409
        )

    client = Client(**data['client'])
    client.details = ClientDetails(**data['details']) if (not is_key_null(data, 'details')) else ClientDetails()
    client.address = Address(**data['address']) if (not is_key_null(data, 'address')) else Address()

    client.save()

    if (not is_key_null(data, 'photo')):
        file = ContentFile(b64decode(data['photo']))
        name = str(uuid1()) + ".png"
        client.details.photo.save(name, file, save=True)

    return True 