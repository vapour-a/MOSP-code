import jpype
import jpype.imports

# Auto-generated wrapper for fda
class fdaWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fda(*args, **kwargs)

    def fda(self, $$0):
        return self.obj.fda($$0)

    def c(self, ):
        return fda.c()

    def a(self, $$0, $$1, $$2, $$3):
        return self.obj.a($$0, $$1, $$2, $$3)

    def a(self, $$0, $$1, $$2, $$3, $$4, $$5):
        return self.obj.a($$0, $$1, $$2, $$3, $$4, $$5)

    def a(self, $$0, $$1):
        return self.obj.a($$0, $$1)
