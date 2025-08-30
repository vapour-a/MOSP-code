import jpype
import jpype.imports

# Auto-generated wrapper for bik
class bikWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = bik(*args, **kwargs)

    def a(self, $$0, $$1):
        return bik.a($$0, $$1)

    def a(self, $$0):
        return bik.a($$0)

    def a(self, $$0, $$1, $$2):
        return self.obj.a($$0, $$1, $$2)
