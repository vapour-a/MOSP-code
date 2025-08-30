import jpype
import jpype.imports

# Auto-generated wrapper for fqu
class fquWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fqu(*args, **kwargs)

    def acq(self, "textures/entity/fish/salmon.png"):
        return self.obj.acq("textures/entity/fish/salmon.png")

    def fqu(self, $$0):
        return self.obj.fqu($$0)

    def a(self, $$0):
        return self.obj.a($$0)

    def a(self, $$0, $$1, $$2, $$3, $$4):
        return self.obj.a($$0, $$1, $$2, $$3, $$4)
