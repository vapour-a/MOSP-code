import jpype
import jpype.imports

# Auto-generated wrapper for frf
class frfWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = frf(*args, **kwargs)

    def acq(self, "textures/entity/squid/squid.png"):
        return self.obj.acq("textures/entity/squid/squid.png")

    def frf(self, $$0, $$1):
        return self.obj.frf($$0, $$1)

    def a(self, $$0):
        return self.obj.a($$0)

    def a(self, $$0, $$1, $$2, $$3, $$4):
        return self.obj.a($$0, $$1, $$2, $$3, $$4)

    def a(self, $$0, $$1):
        return self.obj.a($$0, $$1)
