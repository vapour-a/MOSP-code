import jpype
import jpype.imports

# Auto-generated wrapper for ftv
class ftvWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = ftv(*args, **kwargs)

    def acq(self, "textures/entity/wolf/wolf_collar.png"):
        return self.obj.acq("textures/entity/wolf/wolf_collar.png")

    def ftv(self, fqt<bso, $$0):
        return self.obj.ftv(fqt<bso, $$0)

    def a(self, $$0, $$1, $$2, $$3, $$4, $$5, $$6, $$7, $$8, $$9):
        return self.obj.a($$0, $$1, $$2, $$3, $$4, $$5, $$6, $$7, $$8, $$9)
