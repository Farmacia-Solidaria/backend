import os
class ActionError(Exception):

    def __init__(self, information, status=400, where="undefined") -> None:
        self.information = information
        self.status = status
        self.where = self.where

        if where == "undefined" and 'NAME' in os.environ:
            self.where = os.environ['NAME'] 

        super().__init__(self.information)

    pass