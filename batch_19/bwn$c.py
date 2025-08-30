import jpype
import jpype.imports

# Auto-generated wrapper for c
class cWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = c(*args, **kwargs)

    def c(self, $$0, $$1):
        return self.obj.c($$0, $$1)

    def a(self, ):
        return self.obj.a()
