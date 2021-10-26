from asgiref.sync import sync_to_async

from modules.data.models import Client, ClientDetails, Address

from common.utils.validation import is_key_null

@sync_to_async
def register_client(data):
    client = Client(**data['client'])

    if (not is_key_null(data, 'details')): client.details = ClientDetails(**data['details'])
    if (not is_key_null(data, 'address')): client.address = Address(**data['address'])

    client.save()

    return True 