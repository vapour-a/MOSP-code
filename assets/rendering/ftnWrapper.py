import jpype
import jpype.imports

# Auto-generated wrapper for ftn
class ftnWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = ftn(*args, **kwargs)

    def acq(self, "textures/entity/trident_riptide.png"):
        return self.obj.acq("textures/entity/trident_riptide.png")

    def ftn(self, fqt<T, $$0, $$1):
        return self.obj.ftn(fqt<T, $$0, $$1)

    def a(self, ):
        return ftn.a()

    def fem(self, ):
        return self.obj.fem()

    def a(self, $$0, $$1, $$2, $$3, $$4, $$5, $$6, $$7, $$8, $$9):
        return self.obj.a($$0, $$1, $$2, $$3, $$4, $$5, $$6, $$7, $$8, $$9)
