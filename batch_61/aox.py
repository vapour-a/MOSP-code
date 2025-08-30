import jpype
import jpype.imports

# Auto-generated wrapper for aox
class aoxWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = aox(*args, **kwargs)

    def create(self, $$0, $$1):
        return self.obj.create($$0, $$1)

    def write(self, $$0, $$1):
        return self.obj.write($$0, $$1)

    def read(self, $$0):
        return self.obj.read($$0)

    def a(self, $$0):
        return self.obj.a($$0)
