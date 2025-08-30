import jpype
import jpype.imports

# Auto-generated wrapper for a
class aWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = a(*args, **kwargs)

    def encode(self, $$0, $$1, $$2):
        return self.obj.encode($$0, $$1, $$2)

    def decode(self, $$0, $$1):
        return self.obj.decode($$0, $$1)

    def toString(self, ):
        return self.obj.toString()

    def keys(self, $$0):
        return self.obj.keys($$0)
