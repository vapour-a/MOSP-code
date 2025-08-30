import jpype
import jpype.imports

# Auto-generated wrapper for fcl
class fclWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fcl(*args, **kwargs)

    def fcl(self, $$0):
        return self.obj.fcl($$0)

    def c(self, ):
        return fcl.c()

    def fem(self, ):
        return self.obj.fem()

    def a(self, $$0, $$1, $$2, $$3, $$4, $$5):
        return self.obj.a($$0, $$1, $$2, $$3, $$4, $$5)
