import jpype
import jpype.imports

# Auto-generated wrapper for fdi
class fdiWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fdi(*args, **kwargs)

    def fdi(self, $$0):
        return self.obj.fdi($$0)

    def b(self, ):
        return fdi.b()

    def fem(self, ):
        return self.obj.fem()

    def a(self, $$0, $$1, $$2, $$3, $$4, $$5):
        return self.obj.a($$0, $$1, $$2, $$3, $$4, $$5)

    def a(self, ):
        return self.obj.a()
