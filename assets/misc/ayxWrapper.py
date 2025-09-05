import jpype
import jpype.imports

# Auto-generated wrapper for ayx
class ayxWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = ayx(*args, **kwargs)

    def ayx(self, $$0, $$1):
        return self.obj.ayx($$0, $$1)

    def registerEntities(self, $$0):
        return self.obj.registerEntities($$0)
