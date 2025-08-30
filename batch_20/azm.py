import jpype
import jpype.imports

# Auto-generated wrapper for azm
class azmWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = azm(*args, **kwargs)

    def azm(self, $$0, $$1):
        return self.obj.azm($$0, $$1)

    def registerEntities(self, $$0):
        return self.obj.registerEntities($$0)
