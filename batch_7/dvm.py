import jpype
import jpype.imports

# Auto-generated wrapper for dvm
class dvmWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = dvm(*args, **kwargs)

    def dvm(self, $$0):
        return self.obj.dvm($$0)

    def a(self, $$0, $$1, $$2, $$3, $$4, $$5):
        return self.obj.a($$0, $$1, $$2, $$3, $$4, $$5)

    def a(self, ):
        return self.obj.a()
