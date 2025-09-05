import jpype
import jpype.imports

# Auto-generated wrapper for ig
class igWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = ig(*args, **kwargs)

    def dispense(self, $$0, $$1):
        return self.obj.dispense($$0, $$1)

    def a(self, $$0, $$1):
        return self.obj.a($$0, $$1)

    def a(self, $$0, $$1, $$2, $$3, $$4):
        return ig.a($$0, $$1, $$2, $$3, $$4)

    def bvh(self, $$0, $$5, $$6, $$7, $$1):
        return self.obj.bvh($$0, $$5, $$6, $$7, $$1)

    def a(self, $$0):
        return self.obj.a($$0)

    def a(self, $$0, $$1):
        return self.obj.a($$0, $$1)
