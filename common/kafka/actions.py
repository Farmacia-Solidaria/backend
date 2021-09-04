import random
import functools
from typing import Callable

class ActionHandler():

    actions: dict = {}
    default_function: Callable = None
    on_error: Callable = lambda: False

    def register(self, func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        
        self.actions[func.__name__] = wrapper
        return wrapper

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
        
    
    def get_action(self, action):
        if action in self.actions:
            return self.actions[action]

        if self.default_function != None:
            return self.default_function
        
        