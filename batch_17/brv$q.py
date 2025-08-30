import jpype
import jpype.imports

# Auto-generated wrapper for q
class qWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = q(*args, **kwargs)

    def q(self, parambrv, $$0, $$1):
        return self.obj.q(parambrv, $$0, $$1)

    def c(self, ):
        return self.obj.c()

    def a(self, ):
        return self.obj.a()

    def b(self, ):
        return self.obj.b()

    def h(self, ):
        return self.obj.h()
