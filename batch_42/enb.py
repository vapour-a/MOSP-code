import jpype
import jpype.imports

# Auto-generated wrapper for enb
class enbWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = enb(*args, **kwargs)

    def a(self, $$0, $$1):
        return self.obj.a($$0, $$1)

    def a(self, $$0):
        return self.obj.a($$0)

    def g(self, $$0):
        return enb.g($$0)

    def IncompatibleClassChangeError(self, ):
        return self.obj.IncompatibleClassChangeError()

    def IncompatibleClassChangeError(self, ):
        return self.obj.IncompatibleClassChangeError()

    def b(self, ):
        return self.obj.b()

    def a(self, $$0):
        return self.obj.a($$0)
