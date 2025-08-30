import jpype
import jpype.imports

# Auto-generated wrapper for ayu
class ayuWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = ayu(*args, **kwargs)

    def ayu(self, $$0, $$1):
        return self.obj.ayu($$0, $$1)

    def registerEntities(self, $$0):
        return self.obj.registerEntities($$0)
