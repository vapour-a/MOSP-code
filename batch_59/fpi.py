import jpype
import jpype.imports

# Auto-generated wrapper for fpi
class fpiWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fpi(*args, **kwargs)

    def acq(self, "textures/entity/ghast/ghast.png"):
        return self.obj.acq("textures/entity/ghast/ghast.png")

    def acq(self, "textures/entity/ghast/ghast_shooting.png"):
        return self.obj.acq("textures/entity/ghast/ghast_shooting.png")

    def fpi(self, $$0):
        return self.obj.fpi($$0)

    def a(self, $$0):
        return self.obj.a($$0)

    def a(self, $$0, $$1, $$2):
        return self.obj.a($$0, $$1, $$2)
