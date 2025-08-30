import jpype
import jpype.imports

# Auto-generated wrapper for fir
class firWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fir(*args, **kwargs)

    def b(self, ):
        return self.obj.b()

    def a(self, ):
        return self.obj.a()

    def a(self, $$0):
        return self.obj.a($$0)

    def a(self, $$0, $$1, $$2, $$3, $$4, $$5, $$6, $$7):
        return self.obj.a($$0, $$1, $$2, $$3, $$4, $$5, $$6, $$7)

    def fir(self, $$1, $$2, $$3, $$4):
        return self.obj.fir($$1, $$2, $$3, $$4)
