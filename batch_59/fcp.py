import jpype
import jpype.imports

# Auto-generated wrapper for fcp
class fcpWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fcp(*args, **kwargs)

    def fcp(self, $$0, $$1, $$2, $$3, $$4, $$5, $$6):
        return self.obj.fcp($$0, $$1, $$2, $$3, $$4, $$5, $$6)

    def a(self, $$0, $$1):
        return fcp.a($$0, $$1)

    def fem(self, ):
        return self.obj.fem()

    def a(self, ):
        return self.obj.a()

    def b(self, ):
        return self.obj.b()

    def a(self, $$0, $$1, $$2, $$3, $$4, $$5):
        return self.obj.a($$0, $$1, $$2, $$3, $$4, $$5)
