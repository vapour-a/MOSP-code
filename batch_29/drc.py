import jpype
import jpype.imports

# Auto-generated wrapper for drc
class drcWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = drc(*args, **kwargs)

    def drc(self, $$0, $$1, $$2):
        return self.obj.drc($$0, $$1, $$2)

    def a(self, $$0, $$1, $$2):
        return drc.a($$0, $$1, $$2)

    def drc(self, $$0, $$1, $$2):
        return self.obj.drc($$0, $$1, $$2)

    def a(self, $$0, $$1):
        return self.obj.a($$0, $$1)

    def b(self, ):
        return self.obj.b()
