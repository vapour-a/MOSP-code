import jpype
import jpype.imports

# Auto-generated wrapper for ekf
class ekfWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = ekf(*args, **kwargs)

    def toString(self, ):
        return self.obj.toString()

    def StringBuilder(self, "{"):
        return self.obj.StringBuilder("{")

    def a(self, $$0):
        return ekf.a($$0)

    def b(self, $$0):
        return ekf.b($$0)
