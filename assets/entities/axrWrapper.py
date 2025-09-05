import jpype
import jpype.imports

# Auto-generated wrapper for axr
class axrWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = axr(*args, **kwargs)

    def axr(self, $$0, $$1):
        return self.obj.axr($$0, $$1)

    def registerBlockEntities(self, $$0):
        return self.obj.registerBlockEntities($$0)
