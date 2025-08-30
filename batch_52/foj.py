import jpype
import jpype.imports

# Auto-generated wrapper for foj
class fojWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = foj(*args, **kwargs)

    def acq(self, "textures/entity/fish/cod.png"):
        return self.obj.acq("textures/entity/fish/cod.png")

    def foj(self, $$0):
        return self.obj.foj($$0)

    def a(self, $$0):
        return self.obj.a($$0)

    def a(self, $$0, $$1, $$2, $$3, $$4):
        return self.obj.a($$0, $$1, $$2, $$3, $$4)
