import jpype
import jpype.imports

# Auto-generated wrapper for fti
class ftiWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fti(*args, **kwargs)

    def acq(self, "textures/entity/sheep/sheep_fur.png"):
        return self.obj.acq("textures/entity/sheep/sheep_fur.png")

    def fti(self, fqt<bsh, $$0, $$1):
        return self.obj.fti(fqt<bsh, $$0, $$1)

    def a(self, $$0, $$1, $$2, $$3, $$4, $$5, $$6, $$7, $$8, $$9):
        return self.obj.a($$0, $$1, $$2, $$3, $$4, $$5, $$6, $$7, $$8, $$9)
