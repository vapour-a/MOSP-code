import jpype
import jpype.imports

# Auto-generated wrapper for azp
class azpWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = azp(*args, **kwargs)

    def azp(self, $$0, $$1):
        return self.obj.azp($$0, $$1)

    def registerEntities(self, $$0):
        return self.obj.registerEntities($$0)
