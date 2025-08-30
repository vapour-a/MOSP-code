import jpype
import jpype.imports

# Auto-generated wrapper for dpj
class dpjWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = dpj(*args, **kwargs)

    def a(self, ):
        return self.obj.a()

    def dpj(self, $$0):
        return self.obj.dpj($$0)

    def a(self, $$0):
        return self.obj.a($$0)

    def a(self, $$0, $$1, $$2):
        return dpj.a($$0, $$1, $$2)
