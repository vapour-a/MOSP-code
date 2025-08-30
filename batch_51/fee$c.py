import jpype
import jpype.imports

# Auto-generated wrapper for c
class cWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = c(*args, **kwargs)

    def c(self, $$0, $$1, $$2, $$3, $$4):
        return self.obj.c($$0, $$1, $$2, $$3, $$4)

    def Vector3f(self, $$0, $$1, $$2):
        return self.obj.Vector3f($$0, $$1, $$2)

    def a(self, $$0, $$1):
        return self.obj.a($$0, $$1)

    def c(self, this.a, $$0, $$1):
        return self.obj.c(this.a, $$0, $$1)

    def c(self, $$0, $$1, $$2):
        return self.obj.c($$0, $$1, $$2)
