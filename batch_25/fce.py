import jpype
import jpype.imports

# Auto-generated wrapper for fce
class fceWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fce(*args, **kwargs)

    def fce(self, $$0):
        return self.obj.fce($$0)

    def c(self, ):
        return fce.c()

    def fem(self, ):
        return self.obj.fem()

    def a(self, $$0, $$1, $$2, $$3):
        return self.obj.a($$0, $$1, $$2, $$3)

    def a(self, $$0, $$1, $$2, $$3, $$4, $$5):
        return self.obj.a($$0, $$1, $$2, $$3, $$4, $$5)

    def if(self, 20):
        return self.obj.if(20)
