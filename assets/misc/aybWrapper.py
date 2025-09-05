import jpype
import jpype.imports

# Auto-generated wrapper for ayb
class aybWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = ayb(*args, **kwargs)

    def ayb(self, $$0, $$1):
        return self.obj.ayb($$0, $$1)

    def registerEntities(self, $$0):
        return self.obj.registerEntities($$0)
