import jpype
import jpype.imports

# Auto-generated wrapper for ckl
class cklWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = ckl(*args, **kwargs)

    def ckl(self, $$0, $$1):
        return self.obj.ckl($$0, $$1)

    def a(self, $$0):
        return self.obj.a($$0)

    def b(self, $$0):
        return self.obj.b($$0)

    def a(self, ):
        return self.obj.a()
