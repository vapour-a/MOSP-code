import jpype
import jpype.imports

# Auto-generated wrapper for bda
class bdaWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = bda(*args, **kwargs)

    def a(self, $$0, $$1):
        return bda.a($$0, $$1)

    def a(self, ):
        return self.obj.a()

    def b(self, ):
        return self.obj.b()

    def c(self, ):
        return self.obj.c()
