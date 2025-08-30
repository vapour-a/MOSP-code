import jpype
import jpype.imports

# Auto-generated wrapper for jt
class jtWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = jt(*args, **kwargs)

    def a(self, $$0, $$1):
        return self.obj.a($$0, $$1)

    def acq(self, "textures/gui/advancements/backgrounds/end.png"):
        return self.obj.acq("textures/gui/advancements/backgrounds/end.png")
