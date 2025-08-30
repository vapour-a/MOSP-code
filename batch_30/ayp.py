import jpype
import jpype.imports

# Auto-generated wrapper for ayp
class aypWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = ayp(*args, **kwargs)

    def ayp(self, $$0, $$1):
        return self.obj.ayp($$0, $$1)

    def registerEntities(self, $$0):
        return self.obj.registerEntities($$0)
