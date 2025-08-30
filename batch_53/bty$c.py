import jpype
import jpype.imports

# Auto-generated wrapper for c
class cWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = c(*args, **kwargs)

    def a(self, $$0, $$1):
        return self.obj.a($$0, $$1)

    def a(self, $$0, $$1, $$2):
        return self.obj.a($$0, $$1, $$2)

    def b(self, $$0, $$1, $$2):
        return self.obj.b($$0, $$1, $$2)

    def c(self, $$0, $$1, $$2):
        return self.obj.c($$0, $$1, $$2)
