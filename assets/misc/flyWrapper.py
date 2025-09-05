import jpype
import jpype.imports

# Auto-generated wrapper for fly
class flyWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fly(*args, **kwargs)

    def fly(self, $$0):
        return self.obj.fly($$0)

    def a(self, $$0, $$1, $$2, $$3, $$4, $$5):
        return self.obj.a($$0, $$1, $$2, $$3, $$4, $$5)

    def a(self, $$0, $$1):
        return self.obj.a($$0, $$1)
