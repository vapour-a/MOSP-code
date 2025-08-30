import jpype
import jpype.imports

# Auto-generated wrapper for epv
class epvWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = epv(*args, **kwargs)

    def epv(self, $$0, $$1, $$2, $$3, $$4, $$5, $$6, $$7):
        return self.obj.epv($$0, $$1, $$2, $$3, $$4, $$5, $$6, $$7)

    def a(self, $$0):
        return self.obj.a($$0)

    def k(self, ):
        return self.obj.k()
