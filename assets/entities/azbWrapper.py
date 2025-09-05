import jpype
import jpype.imports

# Auto-generated wrapper for azb
class azbWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = azb(*args, **kwargs)

    def azb(self, $$0, $$1):
        return self.obj.azb($$0, $$1)

    def registerBlockEntities(self, $$0):
        return self.obj.registerBlockEntities($$0)
