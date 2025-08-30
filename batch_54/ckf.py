import jpype
import jpype.imports

# Auto-generated wrapper for ckf
class ckfWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = ckf(*args, **kwargs)

    def ckf(self, $$0, $$1):
        return self.obj.ckf($$0, $$1)

    def a(self, $$0):
        return self.obj.a($$0)

    def b(self, $$0):
        return self.obj.b($$0)

    def a(self, ):
        return self.obj.a()

    def a(self, $$0):
        return self.obj.a($$0)
