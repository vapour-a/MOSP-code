import jpype
import jpype.imports

# Auto-generated wrapper for fdk
class fdkWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fdk(*args, **kwargs)

    def acq(self, "textures/entity/trident.png"):
        return self.obj.acq("textures/entity/trident.png")

    def fdk(self, $$0):
        return self.obj.fdk($$0)

    def a(self, ):
        return fdk.a()

    def fem(self, ):
        return self.obj.fem()

    def a(self, $$0, $$1, $$2, $$3, $$4, $$5, $$6, $$7):
        return self.obj.a($$0, $$1, $$2, $$3, $$4, $$5, $$6, $$7)
