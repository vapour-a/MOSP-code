import jpype
import jpype.imports

# Auto-generated wrapper for eex
class eexWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = eex(*args, **kwargs)

    def eex(self, $$0, $$1):
        return self.obj.eex($$0, $$1)

    def getDouble(self, $$0):
        return self.obj.getDouble($$0)

    def size(self, ):
        return self.obj.size()
