import jpype
import jpype.imports

# Auto-generated wrapper for frl
class frlWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = frl(*args, **kwargs)

    def acq(self, "textures/entity/projectiles/arrow.png"):
        return self.obj.acq("textures/entity/projectiles/arrow.png")

    def acq(self, "textures/entity/projectiles/tipped_arrow.png"):
        return self.obj.acq("textures/entity/projectiles/tipped_arrow.png")

    def frl(self, $$0):
        return self.obj.frl($$0)

    def a(self, $$0):
        return self.obj.a($$0)
