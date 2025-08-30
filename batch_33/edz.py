import jpype
import jpype.imports

# Auto-generated wrapper for edz
class edzWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = edz(*args, **kwargs)

    def toString(self, ):
        return self.obj.toString()

    def hashCode(self, ):
        return self.obj.hashCode()

    def edz(self, $$0, $$1):
        return self.obj.edz($$0, $$1)

    def equals(self, $$0):
        return self.obj.equals($$0)

    def a(self, ):
        return self.obj.a()

    def b(self, ):
        return self.obj.b()
