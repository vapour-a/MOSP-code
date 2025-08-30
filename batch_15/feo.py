import jpype
import jpype.imports

# Auto-generated wrapper for feo
class feoWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = feo(*args, **kwargs)

    def feo(self, $$0, $$1):
        return self.obj.feo($$0, $$1)

    def a(self, ):
        return self.obj.a()

    def b(self, ):
        return self.obj.b()

    def toString(self, ):
        return self.obj.toString()
