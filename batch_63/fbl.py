import jpype
import jpype.imports

# Auto-generated wrapper for fbl
class fblWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fbl(*args, **kwargs)

    def fbl(self, $$0):
        return self.obj.fbl($$0)

    def c(self, ):
        return fbl.c()

    def fem(self, ):
        return self.obj.fem()

    def a(self, $$0, $$1, $$2, $$3, $$4, $$5):
        return self.obj.a($$0, $$1, $$2, $$3, $$4, $$5)
