import jpype
import jpype.imports

# Auto-generated wrapper for fcu
class fcuWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fcu(*args, **kwargs)

    def fcu(self, $$0):
        return self.obj.fcu($$0)

    def c(self, ):
        return fcu.c()

    def fem(self, ):
        return self.obj.fem()

    def fei(self, 0.6F):
        return self.obj.fei(0.6F)

    def fei(self, 1.75F):
        return self.obj.fei(1.75F)

    def fei(self, 0.5F):
        return self.obj.fei(0.5F)

    def a(self, $$0, $$1, $$2, $$3):
        return self.obj.a($$0, $$1, $$2, $$3)

    def a(self, $$0, $$1, $$2, $$3, $$4, $$5):
        return self.obj.a($$0, $$1, $$2, $$3, $$4, $$5)
