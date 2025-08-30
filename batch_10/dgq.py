import jpype
import jpype.imports

# Auto-generated wrapper for dgq
class dgqWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = dgq(*args, **kwargs)

    def a(self, $$0, $$1):
        return self.obj.a($$0, $$1)

    def c(self, $$0):
        return dgq.c($$0)

    def IllegalArgumentException(self, $$0):
        return self.obj.IllegalArgumentException($$0)

    def a(self, $$0, $$1):
        return self.obj.a($$0, $$1)

    def b(self, paramsf):
        return self.obj.b(paramsf)

    def a(self, paramsf, paramT):
        return self.obj.a(paramsf, paramT)

    def a(self, ):
        return self.obj.a()
