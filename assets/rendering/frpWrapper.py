import jpype
import jpype.imports

# Auto-generated wrapper for frp
class frpWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = frp(*args, **kwargs)

    def acq(self, "textures/entity/turtle/big_sea_turtle.png"):
        return self.obj.acq("textures/entity/turtle/big_sea_turtle.png")

    def frp(self, $$0):
        return self.obj.frp($$0)

    def a(self, $$0, $$1, $$2, $$3, $$4, $$5):
        return self.obj.a($$0, $$1, $$2, $$3, $$4, $$5)

    def a(self, $$0):
        return self.obj.a($$0)
