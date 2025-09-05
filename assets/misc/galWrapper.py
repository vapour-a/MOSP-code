import jpype
import jpype.imports

# Auto-generated wrapper for gal
class galWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = gal(*args, **kwargs)

    def gal(self, $$0, $$1, $$2, $$3):
        return self.obj.gal($$0, $$1, $$2, $$3)

    def a(self, $$0, $$1, $$2, $$3):
        return self.obj.a($$0, $$1, $$2, $$3)

    def a(self, ):
        return self.obj.a()
