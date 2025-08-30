import jpype
import jpype.imports

# Auto-generated wrapper for axi
class axiWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = axi(*args, **kwargs)

    def axi(self, $$0, $$1):
        return self.obj.axi($$0, $$1)

    def registerEntities(self, $$0):
        return self.obj.registerEntities($$0)
