import jpype
import jpype.imports

# Auto-generated wrapper for fos
class fosWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fos(*args, **kwargs)

    def acq(self, "textures/entity/end_crystal/end_crystal.png"):
        return self.obj.acq("textures/entity/end_crystal/end_crystal.png")

    def fos(self, $$0):
        return self.obj.fos($$0)

    def a(self, ):
        return fos.a()

    def fem(self, ):
        return self.obj.fem()

    def a(self, $$0, $$1, $$2, $$3, $$4, $$5):
        return self.obj.a($$0, $$1, $$2, $$3, $$4, $$5)

    def Quaternionf(self, ):
        return self.obj.Quaternionf()

    def Quaternionf(self, ):
        return self.obj.Quaternionf()

    def Quaternionf(self, ):
        return self.obj.Quaternionf()

    def a(self, $$0, $$1):
        return fos.a($$0, $$1)

    def a(self, $$0):
        return self.obj.a($$0)

    def a(self, $$0, $$1, $$2, $$3, $$4):
        return self.obj.a($$0, $$1, $$2, $$3, $$4)
