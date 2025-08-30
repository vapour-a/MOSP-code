import jpype
import jpype.imports

# Auto-generated wrapper for fpx
class fpxWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fpx(*args, **kwargs)

    def acq(self, "textures/entity/lead_knot.png"):
        return self.obj.acq("textures/entity/lead_knot.png")

    def fpx(self, $$0):
        return self.obj.fpx($$0)

    def a(self, $$0, $$1, $$2, $$3, $$4, $$5):
        return self.obj.a($$0, $$1, $$2, $$3, $$4, $$5)

    def a(self, $$0):
        return self.obj.a($$0)
