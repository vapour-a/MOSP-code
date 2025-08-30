import jpype
import jpype.imports

# Auto-generated wrapper for fcv
class fcvWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fcv(*args, **kwargs)

    def fcv(self, $$0):
        return self.obj.fcv($$0)

    def c(self, ):
        return fcv.c()

    def a(self, $$0, $$1, $$2, $$3):
        return self.obj.a($$0, $$1, $$2, $$3)

    def a(self, $$0, $$1, $$2, $$3, $$4, $$5):
        return self.obj.a($$0, $$1, $$2, $$3, $$4, $$5)
