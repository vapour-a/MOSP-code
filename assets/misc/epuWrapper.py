import jpype
import jpype.imports

# Auto-generated wrapper for epu
class epuWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = epu(*args, **kwargs)

    def epu(self, $$0, $$1, $$2):
        return self.obj.epu($$0, $$1, $$2)

    def epu(self, $$0, $$1, $$2, $$3, $$4):
        return self.obj.epu($$0, $$1, $$2, $$3, $$4)

    def a(self, $$0):
        return self.obj.a($$0)

    def b(self, $$0, $$1, $$2, $$3):
        return self.obj.b($$0, $$1, $$2, $$3)
