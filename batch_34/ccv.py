import jpype
import jpype.imports

# Auto-generated wrapper for ccv
class ccvWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = ccv(*args, **kwargs)

    def ccv(self, $$0, $$1, $$2, $$3):
        return self.obj.ccv($$0, $$1, $$2, $$3)

    def a(self, $$0):
        return self.obj.a($$0)
