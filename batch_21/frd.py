import jpype
import jpype.imports

# Auto-generated wrapper for frd
class frdWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = frd(*args, **kwargs)

    def acq(self, "textures/entity/projectiles/spectral_arrow.png"):
        return self.obj.acq("textures/entity/projectiles/spectral_arrow.png")

    def frd(self, $$0):
        return self.obj.frd($$0)

    def a(self, $$0):
        return self.obj.a($$0)
