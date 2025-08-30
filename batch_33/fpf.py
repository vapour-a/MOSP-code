import jpype
import jpype.imports

# Auto-generated wrapper for fpf
class fpfWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fpf(*args, **kwargs)

    def acq(self, "textures/entity/fishing_hook.png"):
        return self.obj.acq("textures/entity/fishing_hook.png")

    def fpf(self, $$0):
        return self.obj.fpf($$0)

    def a(self, $$0, $$1, $$2, $$3, $$4, $$5):
        return self.obj.a($$0, $$1, $$2, $$3, $$4, $$5)

    def a(self, $$0, $$1):
        return fpf.a($$0, $$1)

    def a(self, $$0, $$1, $$2, $$3, $$4, $$5, $$6, $$7):
        return fpf.a($$0, $$1, $$2, $$3, $$4, $$5, $$6, $$7)

    def a(self, $$0, $$1, $$2, $$3, $$4, $$5, $$6):
        return fpf.a($$0, $$1, $$2, $$3, $$4, $$5, $$6)

    def a(self, $$0):
        return self.obj.a($$0)
