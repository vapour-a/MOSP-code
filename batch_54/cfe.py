import jpype
import jpype.imports

# Auto-generated wrapper for cfe
class cfeWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = cfe(*args, **kwargs)

    def cfe(self, $$0):
        return self.obj.cfe($$0)

    def a(self, $$0, $$1, $$2, $$3):
        return self.obj.a($$0, $$1, $$2, $$3)

    def a(self, $$0, $$1):
        return cfe.a($$0, $$1)

    def a(self, $$0, $$1):
        return cfe.a($$0, $$1)

    def a(self, $$0):
        return cfe.a($$0)
