import jpype
import jpype.imports

# Auto-generated wrapper for azj
class azjWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = azj(*args, **kwargs)

    def azj(self, $$0, $$1):
        return self.obj.azj($$0, $$1)

    def registerEntities(self, $$0):
        return self.obj.registerEntities($$0)
