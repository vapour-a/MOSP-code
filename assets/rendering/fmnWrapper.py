import jpype
import jpype.imports

# Auto-generated wrapper for fmn
class fmnWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fmn(*args, **kwargs)

    def acq(self, "textures/environment/end_sky.png"):
        return self.obj.acq("textures/environment/end_sky.png")

    def acq(self, "textures/entity/end_portal.png"):
        return self.obj.acq("textures/entity/end_portal.png")

    def fmn(self, $$0):
        return self.obj.fmn($$0)

    def a(self, $$0, $$1, $$2, $$3, $$4, $$5):
        return self.obj.a($$0, $$1, $$2, $$3, $$4, $$5)

    def a(self, $$0, $$1, $$2):
        return self.obj.a($$0, $$1, $$2)

    def a(self, $$0, $$1, $$2, $$3, $$4, $$5, $$6, $$7, $$8, $$9, $$10, $$11):
        return self.obj.a($$0, $$1, $$2, $$3, $$4, $$5, $$6, $$7, $$8, $$9, $$10, $$11)

    def b(self, ):
        return self.obj.b()

    def c(self, ):
        return self.obj.c()

    def d(self, ):
        return self.obj.d()
