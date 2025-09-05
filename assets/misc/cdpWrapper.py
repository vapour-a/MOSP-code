import jpype
import jpype.imports

# Auto-generated wrapper for cdp
class cdpWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = cdp(*args, **kwargs)

    def cdp(self, $$0, $$1, $$2):
        return self.obj.cdp($$0, $$1, $$2)

    def a(self, $$0, $$1):
        return cdp.a($$0, $$1)

    def b(self, ):
        return self.obj.b()

    def a(self, $$0, $$1, $$2, $$3):
        return self.obj.a($$0, $$1, $$2, $$3)
