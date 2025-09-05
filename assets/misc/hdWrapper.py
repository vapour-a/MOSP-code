import jpype
import jpype.imports

# Auto-generated wrapper for hd
class hdWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = hd(*args, **kwargs)

    def hd(self, $$0, $$1):
        return self.obj.hd($$0, $$1)

    def a(self, $$0, $$1):
        return hd.a($$0, $$1)

    def hd(self, $$0, $$1):
        return self.obj.hd($$0, $$1)

    def a(self, ):
        return self.obj.a()

    def b(self, ):
        return self.obj.b()

    def equals(self, $$0):
        return self.obj.equals($$0)

    def hashCode(self, ):
        return self.obj.hashCode()

    def toString(self, ):
        return self.obj.toString()
