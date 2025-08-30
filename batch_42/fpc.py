import jpype
import jpype.imports

# Auto-generated wrapper for fpc
class fpcWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fpc(*args, **kwargs)

    def acq(self, "textures/entity/experience_orb.png"):
        return self.obj.acq("textures/entity/experience_orb.png")

    def fpc(self, $$0):
        return self.obj.fpc($$0)

    def a(self, $$0, $$1):
        return self.obj.a($$0, $$1)

    def a(self, $$0, $$1, $$2, $$3, $$4, $$5):
        return self.obj.a($$0, $$1, $$2, $$3, $$4, $$5)

    def a(self, $$0, $$1, $$2, $$3, $$4, $$5, $$6, $$7, $$8, $$9, $$10):
        return fpc.a($$0, $$1, $$2, $$3, $$4, $$5, $$6, $$7, $$8, $$9, $$10)

    def a(self, $$0):
        return self.obj.a($$0)
