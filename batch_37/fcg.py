import jpype
import jpype.imports

# Auto-generated wrapper for fcg
class fcgWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fcg(*args, **kwargs)

    def fcg(self, $$0):
        return self.obj.fcg($$0)

    def b(self, ):
        return fcg.b()

    def fem(self, ):
        return self.obj.fem()

    def a(self, ):
        return self.obj.a()

    def a(self, $$0, $$1, $$2, $$3, $$4, $$5):
        return self.obj.a($$0, $$1, $$2, $$3, $$4, $$5)
