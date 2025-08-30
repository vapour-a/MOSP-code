import jpype
import jpype.imports

# Auto-generated wrapper for c
class cWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = c(*args, **kwargs)

    def a(self, $$0):
        return self.obj.a($$0)

    def b(self, $$0):
        return self.obj.b($$0)

    def a(self, $$0, $$1, $$2):
        return self.obj.a($$0, $$1, $$2)

    def a(self, ):
        return self.obj.a()

    def c(self, this.c, this.g, this.h, this.i, 0.0D, 0.0D, 0.0D, this.G, this.a):
        return self.obj.c(this.c, this.g, this.h, this.i, 0.0D, 0.0D, 0.0D, this.G, this.a)
