import jpype
import jpype.imports

# Auto-generated wrapper for fri
class friWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fri(*args, **kwargs)

    def acq(self, "textures/entity/tadpole/tadpole.png"):
        return self.obj.acq("textures/entity/tadpole/tadpole.png")

    def fri(self, $$0):
        return self.obj.fri($$0)

    def a(self, $$0):
        return self.obj.a($$0)
