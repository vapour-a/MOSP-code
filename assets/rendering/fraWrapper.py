import jpype
import jpype.imports

# Auto-generated wrapper for fra
class fraWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fra(*args, **kwargs)

    def acq(self, "textures/entity/slime/slime.png"):
        return self.obj.acq("textures/entity/slime/slime.png")

    def fra(self, $$0):
        return self.obj.fra($$0)

    def a(self, $$0, $$1, $$2, $$3, $$4, $$5):
        return self.obj.a($$0, $$1, $$2, $$3, $$4, $$5)

    def a(self, $$0, $$1, $$2):
        return self.obj.a($$0, $$1, $$2)

    def a(self, $$0):
        return self.obj.a($$0)
