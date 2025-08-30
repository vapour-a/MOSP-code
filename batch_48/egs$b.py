import jpype
import jpype.imports

# Auto-generated wrapper for b
class bWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = b(*args, **kwargs)

    def a(self, $$0, $$1):
        return b.a($$0, $$1)

    def b(self, $$0, $$1):
        return self.obj.b($$0, $$1)

    def equals(self, $$0):
        return self.obj.equals($$0)

    def hashCode(self, ):
        return self.obj.hashCode()

    def toString(self, ):
        return self.obj.toString()
