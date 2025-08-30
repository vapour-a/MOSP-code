import jpype
import jpype.imports

# Auto-generated wrapper for fpb
class fpbWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fpb(*args, **kwargs)

    def acq(self, "textures/entity/illager/evoker.png"):
        return self.obj.acq("textures/entity/illager/evoker.png")

    def fpb(self, $$0):
        return self.obj.fpb($$0)

    def a(self, $$0, $$1, $$2, $$3, $$4, $$5, $$6, $$7, $$8, $$9):
        return self.obj.a($$0, $$1, $$2, $$3, $$4, $$5, $$6, $$7, $$8, $$9)

    def a(self, $$0):
        return self.obj.a($$0)
