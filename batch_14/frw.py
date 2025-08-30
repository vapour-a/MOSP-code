import jpype
import jpype.imports

# Auto-generated wrapper for frw
class frwWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = frw(*args, **kwargs)

    def acq(self, "textures/entity/witch.png"):
        return self.obj.acq("textures/entity/witch.png")

    def frw(self, $$0):
        return self.obj.frw($$0)

    def a(self, $$0, $$1, $$2, $$3, $$4, $$5):
        return self.obj.a($$0, $$1, $$2, $$3, $$4, $$5)

    def a(self, $$0):
        return self.obj.a($$0)

    def a(self, $$0, $$1, $$2):
        return self.obj.a($$0, $$1, $$2)
