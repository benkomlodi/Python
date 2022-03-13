class FunctionHandler:
    def __init__(self, name, handlers = dict()) -> None:
        self.name = name
        self.handlers = handlers
    def add_function(self, key, handler):
        self.handlers[key] = handler
    def get_function(self, key):
        return self.handlers[key]