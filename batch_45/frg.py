import jpype
import jpype.imports

# Auto-generated wrapper for frg
class frgWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = frg(*args, **kwargs)

    def acq(self, "textures/entity/skeleton/stray.png"):
        return self.obj.acq("textures/entity/skeleton/stray.png")

    def frg(self, $$0):
        return self.obj.frg($$0)

    def a(self, $$0):
        return self.obj.a($$0)
