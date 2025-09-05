import jpype
import jpype.imports

# Auto-generated wrapper for drn
class drnWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = drn(*args, **kwargs)

    def drn(self, $$0):
        return self.obj.drn($$0)

    def a(self, $$0):
        return drn.a($$0)

    def drn(self, $$0):
        return self.obj.drn($$0)

    def a(self, $$0, $$1, $$2):
        return self.obj.a($$0, $$1, $$2)

    def b(self, ):
        return self.obj.b()
