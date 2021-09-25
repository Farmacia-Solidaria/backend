import random
import functools
from typing import Callable

class ActionHandler():

    actions: dict = {
        "post": {},
        "get": {},
        "put": {},
        "patch": {},
        "delete": {},
        "options": {},
        "head": {},
    }
    default_function: Callable = None
    on_error: Callable = lambda: False

    def register(self, method:str = "post"):
        def decorator(func):

            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)
            
            self.actions[method.lower()][func.__name__] = wrapper
            return wrapper
            
        return decorator

    def default(self, func):
        self.default_function = func

        return func

    def register_error_handler(self, func):
        self.on_error = func
        
        return func

    def run_action(self, action, *args, **kwargs):
        try:
            return self.get_action(action)(*args, **kwargs)
        except Exception as ex:
            return self.on_error(action, ex, *args, **kwargs)
        
    
    def get_action(self, method, action):
        if method in self.actions:
            if action in self.actions[method]:
                return self.actions[method][action]

        if self.default_function != None:
            return self.default_function
        
        