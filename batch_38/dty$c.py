import jpype
import jpype.imports

# Auto-generated wrapper for c
class cWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = c(*args, **kwargs)

    def c(self, $$0, $$1, $$2, $$3):
        return self.obj.c($$0, $$1, $$2, $$3)

    def c(self, $$0):
        return self.obj.c($$0)

    def a(self, $$0, $$1, $$2):
        return self.obj.a($$0, $$1, $$2)

    def a(self, $$0, $$1, $$2, $$3, $$4, $$5, $$6):
        return c.a($$0, $$1, $$2, $$3, $$4, $$5, $$6)

    def c(self, $$6, $$1, $$7, $$5):
        return self.obj.c($$6, $$1, $$7, $$5)

    def a(self, $$0, $$1, $$2, $$3, $$4, $$5, $$6):
        return self.obj.a($$0, $$1, $$2, $$3, $$4, $$5, $$6)
