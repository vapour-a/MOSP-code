import jpype
import jpype.imports

# Auto-generated wrapper for azq
class azqWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = azq(*args, **kwargs)

    def azq(self, $$0, $$1):
        return self.obj.azq($$0, $$1)

    def registerEntities(self, $$0):
        return self.obj.registerEntities($$0)
