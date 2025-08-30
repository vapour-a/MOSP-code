import jpype
import jpype.imports

# Auto-generated wrapper for blv
class blvWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = blv(*args, **kwargs)

    def blv(self, $$0, $$1, $$2):
        return self.obj.blv($$0, $$1, $$2)

    def a(self, ):
        return self.obj.a()
