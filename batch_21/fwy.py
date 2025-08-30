import jpype
import jpype.imports

# Auto-generated wrapper for fwy
class fwyWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fwy(*args, **kwargs)

    def fwy(self, $$0, $$1, $$2, $$3):
        return self.obj.fwy($$0, $$1, $$2, $$3)

    def fwy(self, $$0, $$1, $$2):
        return self.obj.fwy($$0, $$1, $$2)

    def fwy(self, $$0, $$1):
        return self.obj.fwy($$0, $$1)

    def c(self, $$0, $$1):
        return fwy.c($$0, $$1)

    def fwy(self, "minecraft", $$0, $$1):
        return self.obj.fwy("minecraft", $$0, $$1)

    def h(self, $$0):
        return fwy.h($$0)

    def f(self, ):
        return self.obj.f()

    def equals(self, $$0):
        return self.obj.equals($$0)

    def hashCode(self, ):
        return self.obj.hashCode()

    def toString(self, ):
        return self.obj.toString()
