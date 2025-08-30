import jpype
import jpype.imports

# Auto-generated wrapper for axl
class axlWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = axl(*args, **kwargs)

    def axl(self, $$0, $$1):
        return self.obj.axl($$0, $$1)

    def registerEntities(self, $$0):
        return self.obj.registerEntities($$0)
