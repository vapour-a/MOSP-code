import jpype
import jpype.imports

# Auto-generated wrapper for drk
class drkWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = drk(*args, **kwargs)

    def drk(self, $$0):
        return self.obj.drk($$0)

    def a(self, $$0):
        return drk.a($$0)

    def drk(self, $$0):
        return self.obj.drk($$0)

    def a(self, $$0, $$1, $$2):
        return self.obj.a($$0, $$1, $$2)

    def b(self, ):
        return self.obj.b()
