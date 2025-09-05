import jpype
import jpype.imports

# Auto-generated wrapper for fco
class fcoWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fco(*args, **kwargs)

    def fco(self, $$0):
        return self.obj.fco($$0)

    def b(self, ):
        return fco.b()

    def fem(self, ):
        return self.obj.fem()

    def a(self, ):
        return self.obj.a()

    def a(self, $$0, $$1, $$2, $$3, $$4, $$5):
        return self.obj.a($$0, $$1, $$2, $$3, $$4, $$5)
