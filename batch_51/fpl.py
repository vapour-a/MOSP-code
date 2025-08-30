import jpype
import jpype.imports

# Auto-generated wrapper for fpl
class fplWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fpl(*args, **kwargs)

    def acq(self, "textures/entity/goat/goat.png"):
        return self.obj.acq("textures/entity/goat/goat.png")

    def fpl(self, $$0):
        return self.obj.fpl($$0)

    def a(self, $$0):
        return self.obj.a($$0)
