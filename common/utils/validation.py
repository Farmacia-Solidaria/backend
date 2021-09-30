
def is_key_null(obj, key):
    if key in obj:
        if obj[key] != "":
            return False
            
    return True