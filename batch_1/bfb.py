import jpype
import jpype.imports

# Auto-generated wrapper for bfb
class bfbWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = bfb(*args, **kwargs)

    def a(self, $$0, $$1):
        return bfb.a($$0, $$1)

    def a(self, $$0):
        return bfb.a($$0)

    def b(self, $$0):
        return bfb.b($$0)

    def c(self, $$0):
        return bfb.c($$0)

    def a(self, $$0, $$1, $$2, $$3, $$4, $$5):
        return bfb.a($$0, $$1, $$2, $$3, $$4, $$5)

    def bfa(self, $$0):
        return self.obj.bfa($$0)
