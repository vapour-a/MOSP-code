import jpype
import jpype.imports

# Auto-generated wrapper for fkh
class fkhWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fkh(*args, **kwargs)

    def acq(self, "textures/misc/underwater.png"):
        return self.obj.acq("textures/misc/underwater.png")

    def a(self, $$0, $$1):
        return fkh.a($$0, $$1)

    def a(self, $$0):
        return fkh.a($$0)

    def a(self, $$0, $$1):
        return fkh.a($$0, $$1)

    def b(self, $$0, $$1):
        return fkh.b($$0, $$1)

    def c(self, $$0, $$1):
        return fkh.c($$0, $$1)
