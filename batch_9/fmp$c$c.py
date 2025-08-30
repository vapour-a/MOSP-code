import jpype
import jpype.imports

# Auto-generated wrapper for c
class cWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = c(*args, **kwargs)

    def c(self, paramc, $$0, $$1):
        return self.obj.c(paramc, $$0, $$1)

    def b(self, ):
        return self.obj.b()

    def a(self, $$0):
        return self.obj.a($$0)

    def a(self, ):
        return self.obj.a()
