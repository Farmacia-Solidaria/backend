import os

def get_public_key():
    return os.environ["PUBLIC_KEY"].replace("\\n", "\n")

def get_private_key():
    return os.environ["PRIVATE_KEY"].replace("\\n", "\n")