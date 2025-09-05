import jpype
import jpype.imports

# Auto-generated wrapper for faz
class fazWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = faz(*args, **kwargs)

    def faz(self, $$0):
        return self.obj.faz($$0)

    def a(self, $$0):
        return faz.a($$0)

    def fem(self, ):
        return self.obj.fem()

    def a(self, ):
        return self.obj.a()

    def a(self, $$0, $$1, $$2, $$3, $$4, $$5):
        return self.obj.a($$0, $$1, $$2, $$3, $$4, $$5)
