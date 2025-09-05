import jpype
import jpype.imports

# Auto-generated wrapper for fob
class fobWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fob(*args, **kwargs)

    def acq(self, "textures/entity/bee/bee_angry.png"):
        return self.obj.acq("textures/entity/bee/bee_angry.png")

    def acq(self, "textures/entity/bee/bee_angry_nectar.png"):
        return self.obj.acq("textures/entity/bee/bee_angry_nectar.png")

    def acq(self, "textures/entity/bee/bee.png"):
        return self.obj.acq("textures/entity/bee/bee.png")

    def acq(self, "textures/entity/bee/bee_nectar.png"):
        return self.obj.acq("textures/entity/bee/bee_nectar.png")

    def fob(self, $$0):
        return self.obj.fob($$0)

    def a(self, $$0):
        return self.obj.a($$0)
