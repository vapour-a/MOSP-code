import jpype
import jpype.imports

# Auto-generated wrapper for chw
class chwWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = chw(*args, **kwargs)

    def a(self, $$0):
        return chw.a($$0)

    def chw(self, $$0):
        return self.obj.chw($$0)

    def chw(self, $$0, $$1):
        return self.obj.chw($$0, $$1)

    def b(self, $$0):
        return self.obj.b($$0)

    def a(self, ):
        return self.obj.a()

    def b(self, ):
        return self.obj.b()
