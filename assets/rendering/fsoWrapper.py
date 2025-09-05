import jpype
import jpype.imports

# Auto-generated wrapper for fso
class fsoWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fso(*args, **kwargs)

    def acq(self, "textures/entity/zombie/drowned_outer_layer.png"):
        return self.obj.acq("textures/entity/zombie/drowned_outer_layer.png")

    def fso(self, fqt<T, $$0, $$1):
        return self.obj.fso(fqt<T, $$0, $$1)

    def a(self, $$0, $$1, $$2, $$3, $$4, $$5, $$6, $$7, $$8, $$9):
        return self.obj.a($$0, $$1, $$2, $$3, $$4, $$5, $$6, $$7, $$8, $$9)
