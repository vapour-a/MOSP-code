import jpype
import jpype.imports

# Auto-generated wrapper for aye
class ayeWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = aye(*args, **kwargs)

    def aye(self, $$0, $$1):
        return self.obj.aye($$0, $$1)

    def registerBlockEntities(self, $$0):
        return self.obj.registerBlockEntities($$0)
