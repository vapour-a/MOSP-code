import jpype
import jpype.imports

# Auto-generated wrapper for dpl
class dplWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = dpl(*args, **kwargs)

    def a(self, $$0, $$1):
        return self.obj.a($$0, $$1)

    def dpl(self, $$1):
        return self.obj.dpl($$1)

    def dpl(self, $$0):
        return self.obj.dpl($$0)

    def a(self, ):
        return self.obj.a()
