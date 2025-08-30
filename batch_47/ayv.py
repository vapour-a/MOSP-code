import jpype
import jpype.imports

# Auto-generated wrapper for ayv
class ayvWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = ayv(*args, **kwargs)

    def ayv(self, $$0, $$1):
        return self.obj.ayv($$0, $$1)

    def registerEntities(self, $$0):
        return self.obj.registerEntities($$0)
