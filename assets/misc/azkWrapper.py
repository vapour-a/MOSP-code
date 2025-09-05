import jpype
import jpype.imports

# Auto-generated wrapper for azk
class azkWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = azk(*args, **kwargs)

    def azk(self, $$0, $$1):
        return self.obj.azk($$0, $$1)

    def registerEntities(self, $$0):
        return self.obj.registerEntities($$0)
