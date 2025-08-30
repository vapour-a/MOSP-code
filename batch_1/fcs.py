import jpype
import jpype.imports

# Auto-generated wrapper for fcs
class fcsWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fcs(*args, **kwargs)

    def fcs(self, $$0):
        return self.obj.fcs($$0)

    def b(self, ):
        return fcs.b()

    def fem(self, ):
        return self.obj.fem()

    def a(self, ):
        return self.obj.a()

    def a(self, $$0, $$1, $$2, $$3, $$4, $$5):
        return self.obj.a($$0, $$1, $$2, $$3, $$4, $$5)

    def a(self, $$0, $$1, $$2, $$3):
        return self.obj.a($$0, $$1, $$2, $$3)

    def if(self, 0):
        return self.obj.if(0)
