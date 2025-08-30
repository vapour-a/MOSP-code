import jpype
import jpype.imports

# Auto-generated wrapper for c
class cWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = c(*args, **kwargs)

    def b(self, ):
        return self.obj.b()

    def a(self, ):
        return self.obj.a()

    def l(self, ):
        return self.obj.l()

    def a(self, $$0, $$1):
        return self.obj.a($$0, $$1)
