import jpype
import jpype.imports

# Auto-generated wrapper for cev
class cevWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = cev(*args, **kwargs)

    def cev(self, $$0):
        return self.obj.cev($$0)

    def i(self, $$0):
        return self.obj.i($$0)

    def d_(self, $$0):
        return self.obj.d_($$0)

    def d(self, $$0):
        return cev.d($$0)

    def qx(self, ):
        return self.obj.qx()

    def a(self, $$0, $$1, $$2, $$3):
        return self.obj.a($$0, $$1, $$2, $$3)

    def a(self, $$0, $$1):
        return cev.a($$0, $$1)

    def a(self, $$0):
        return cev.a($$0)

    def cfz(self, cgc.tC):
        return self.obj.cfz(cgc.tC)
