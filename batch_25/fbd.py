import jpype
import jpype.imports

# Auto-generated wrapper for fbd
class fbdWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fbd(*args, **kwargs)

    def fbd(self, $$0):
        return self.obj.fbd($$0)

    def c(self, ):
        return fbd.c()

    def fei(self, -0.5F):
        return self.obj.fei(-0.5F)

    def a(self, $$0, $$1, $$2, $$3, $$4, $$5):
        return self.obj.a($$0, $$1, $$2, $$3, $$4, $$5)
