import jpype
import jpype.imports

# Auto-generated wrapper for frt
class frtWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = frt(*args, **kwargs)

    def acq(self, "textures/entity/illager/vindicator.png"):
        return self.obj.acq("textures/entity/illager/vindicator.png")

    def frt(self, $$0):
        return self.obj.frt($$0)

    def a(self, $$0, $$1, $$2, $$3, $$4, $$5, $$6, $$7, $$8, $$9):
        return self.obj.a($$0, $$1, $$2, $$3, $$4, $$5, $$6, $$7, $$8, $$9)

    def a(self, $$0):
        return self.obj.a($$0)
