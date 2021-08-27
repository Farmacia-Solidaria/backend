import random
import functools
from typing import Callable

class ActionHandler():

    actions: dict = {}
    default_function: Callable = None

    def register(self, func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        
        self.actions[func.__name__] = wrapper
        return wrapper

    def default(self, func):
        self.default_function = func

        return func

    def run_action(self, action, *args, **kwargs):
        if action in self.actions:
            return self.actions[action](*args, **kwargs)

        if self.default_function != None:
            return self.default_function(*args, **kwargs)
        
        else:
            raise NotImplementedError("Default not implemented")