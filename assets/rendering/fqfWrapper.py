import jpype
import jpype.imports

# Auto-generated wrapper for fqf
class fqfWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fqf(*args, **kwargs)

    def acq(self, "textures/entity/cow/brown_mooshroom.png"):
        return self.obj.acq("textures/entity/cow/brown_mooshroom.png")

    def acq(self, "textures/entity/cow/red_mooshroom.png"):
        return self.obj.acq("textures/entity/cow/red_mooshroom.png")

    def fqf(self, $$0):
        return self.obj.fqf($$0)

    def a(self, $$0):
        return self.obj.a($$0)
