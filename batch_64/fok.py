import jpype
import jpype.imports

# Auto-generated wrapper for fok
class fokWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fok(*args, **kwargs)

    def acq(self, "textures/entity/cow/cow.png"):
        return self.obj.acq("textures/entity/cow/cow.png")

    def fok(self, $$0):
        return self.obj.fok($$0)

    def a(self, $$0):
        return self.obj.a($$0)
