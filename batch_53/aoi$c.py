import jpype
import jpype.imports

# Auto-generated wrapper for c
class cWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = c(*args, **kwargs)

    def toString(self, ):
        return self.obj.toString()

    def hashCode(self, ):
        return self.obj.hashCode()

    def equals(self, $$0):
        return self.obj.equals($$0)

    def a(self, ):
        return self.obj.a()

    def decode(self, $$0, $$1):
        return self.obj.decode($$0, $$1)

    def encode(self, $$0, $$1, $$2):
        return self.obj.encode($$0, $$1, $$2)
