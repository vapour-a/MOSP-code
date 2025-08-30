import jpype
import jpype.imports

# Auto-generated wrapper for flx
class flxWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = flx(*args, **kwargs)

    def a(self, $$0, $$1):
        return self.obj.a($$0, $$1)

    def a(self, $$0):
        return self.obj.a($$0)

    def a(self, ):
        return self.obj.a()
