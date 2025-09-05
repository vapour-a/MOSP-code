import jpype
import jpype.imports

# Auto-generated wrapper for esh
class eshWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = esh(*args, **kwargs)

    def a(self, $$0):
        return self.obj.a($$0)

    def c(self, ):
        return self.obj.c()

    def b(self, paramConsumer):
        return self.obj.b(paramConsumer)
