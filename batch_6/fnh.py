import jpype
import jpype.imports

# Auto-generated wrapper for fnh
class fnhWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fnh(*args, **kwargs)

    def fnh(self, $$0):
        return self.obj.fnh($$0)

    def a(self, $$0, $$1, $$2, $$3, $$4):
        return self.obj.a($$0, $$1, $$2, $$3, $$4)

    def a(self, $$0):
        return self.obj.a($$0)

    def IncompatibleClassChangeError(self, ):
        return self.obj.IncompatibleClassChangeError()

    def Vector3f(self, 0.0F, 0.5F, 0.5F):
        return self.obj.Vector3f(0.0F, 0.5F, 0.5F)
