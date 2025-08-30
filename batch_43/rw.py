import jpype
import jpype.imports

# Auto-generated wrapper for rw
class rwWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = rw(*args, **kwargs)

    def rw(self, $$0):
        return self.obj.rw($$0)

    def a(self, $$0, $$1):
        return self.obj.a($$0, $$1)

    def b(self, ):
        return self.obj.b()
