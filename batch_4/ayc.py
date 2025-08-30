import jpype
import jpype.imports

# Auto-generated wrapper for ayc
class aycWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = ayc(*args, **kwargs)

    def ayc(self, $$0, $$1):
        return self.obj.ayc($$0, $$1)

    def registerEntities(self, $$0):
        return self.obj.registerEntities($$0)
