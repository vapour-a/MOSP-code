import jpype
import jpype.imports

# Auto-generated wrapper for dgk
class dgkWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = dgk(*args, **kwargs)

    def dgk(self, $$0, $$1, $$2):
        return self.obj.dgk($$0, $$1, $$2)

    def a(self, ):
        return self.obj.a()

    def a(self, $$0):
        return self.obj.a($$0)

    def b(self, $$0):
        return self.obj.b($$0)

    def a(self, $$0, $$1, $$2, $$3):
        return self.obj.a($$0, $$1, $$2, $$3)

    def a(self, $$0, $$1, $$2):
        return dgk.a($$0, $$1, $$2)

    def apply(self, param1Int):
        return self.obj.apply(param1Int)
