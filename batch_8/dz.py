import jpype
import jpype.imports

# Auto-generated wrapper for dz
class dzWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = dz(*args, **kwargs)

    def a(self, ):
        return dz.a()

    def dz(self, ):
        return self.obj.dz()

    def a(self, $$0, $$1):
        return self.obj.a($$0, $$1)

    def a(self, $$0):
        return self.obj.a($$0)

    def rl(self, $$0):
        return self.obj.rl($$0)

    def getExamples(self, ):
        return self.obj.getExamples()
