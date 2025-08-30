import jpype
import jpype.imports

# Auto-generated wrapper for cay
class cayWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = cay(*args, **kwargs)

    def a(self, $$0, $$1):
        return cay.a($$0, $$1)

    def a(self, c, $$0, $$1):
        return self.obj.a(c, $$0, $$1)

    def a(self, $$0, $$1, $$2):
        return cay.a($$0, $$1, $$2)

    def a(self, $$0):
        return cay.a($$0)
