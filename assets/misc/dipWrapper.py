import jpype
import jpype.imports

# Auto-generated wrapper for dip
class dipWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = dip(*args, **kwargs)

    def dip(self, $$0):
        return self.obj.dip($$0)

    def a(self, $$0, $$1):
        return self.obj.a($$0, $$1)

    def a(self, ):
        return self.obj.a()
