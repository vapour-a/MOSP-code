import jpype
import jpype.imports

# Auto-generated wrapper for ij
class ijWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = ij(*args, **kwargs)

    def a(self, $$0, $$1):
        return self.obj.a($$0, $$1)

    def a(self, $$0, $$1):
        return ij.a($$0, $$1)

    def b(self, $$0, $$1):
        return ij.b($$0, $$1)

    def eed(self, $$1):
        return self.obj.eed($$1)
