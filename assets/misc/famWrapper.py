import jpype
import jpype.imports

# Auto-generated wrapper for fam
class famWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fam(*args, **kwargs)

    def fam(self, $$0):
        return self.obj.fam($$0)

    def a(self, $$0):
        return fam.a($$0)

    def b(self, ):
        return fam.b()

    def fem(self, ):
        return self.obj.fem()

    def a(self, ):
        return self.obj.a()

    def a(self, $$0, $$1, $$2, $$3, $$4, $$5):
        return self.obj.a($$0, $$1, $$2, $$3, $$4, $$5)
