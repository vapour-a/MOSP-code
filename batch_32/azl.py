import jpype
import jpype.imports

# Auto-generated wrapper for azl
class azlWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = azl(*args, **kwargs)

    def azl(self, $$0, $$1):
        return self.obj.azl($$0, $$1)

    def registerBlockEntities(self, $$0):
        return self.obj.registerBlockEntities($$0)
