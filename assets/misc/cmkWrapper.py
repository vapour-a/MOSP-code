import jpype
import jpype.imports

# Auto-generated wrapper for cmk
class cmkWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = cmk(*args, **kwargs)

    a = cmk.a
    def a(self, $$0):
        return cmk.a($$0)

    def a(self, $$0, $$1):
        return cmk.a($$0, $$1)

    def a(self, ):
        return cmk.a()

    def a(self, 0.5D, 1.0D):
        return self.obj.a(0.5D, 1.0D)
