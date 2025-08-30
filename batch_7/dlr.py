import jpype
import jpype.imports

# Auto-generated wrapper for dlr
class dlrWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = dlr(*args, **kwargs)

    def a(self, $$0):
        return self.obj.a($$0)

    def a(self, $$0, $$1, $$2, $$3):
        return self.obj.a($$0, $$1, $$2, $$3)

    def a(self, $$0, $$1):
        return self.obj.a($$0, $$1)
