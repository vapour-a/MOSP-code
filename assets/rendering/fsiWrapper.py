import jpype
import jpype.imports

# Auto-generated wrapper for fsi
class fsiWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fsi(*args, **kwargs)

    def acq(self, "textures/entity/cat/cat_collar.png"):
        return self.obj.acq("textures/entity/cat/cat_collar.png")

    def fsi(self, fqt<bro, $$0, $$1):
        return self.obj.fsi(fqt<bro, $$0, $$1)

    def a(self, $$0, $$1, $$2, $$3, $$4, $$5, $$6, $$7, $$8, $$9):
        return self.obj.a($$0, $$1, $$2, $$3, $$4, $$5, $$6, $$7, $$8, $$9)
