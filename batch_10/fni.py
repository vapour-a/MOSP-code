import jpype
import jpype.imports

# Auto-generated wrapper for fni
class fniWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fni(*args, **kwargs)

    def fni(self, $$0):
        return self.obj.fni($$0)

    def a(self, $$0, $$1, $$2, $$3, $$4):
        return self.obj.a($$0, $$1, $$2, $$3, $$4)

    def LongOpenHashSet(self, ):
        return self.obj.LongOpenHashSet()
