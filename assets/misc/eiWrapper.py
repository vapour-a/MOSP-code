import jpype
import jpype.imports

# Auto-generated wrapper for ei
class eiWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = ei(*args, **kwargs)

    def a(self, ):
        return ei.a()

    def ei(self, ):
        return self.obj.ei()

    def a(self, $$0, $$1):
        return self.obj.a($$0, $$1)

    def a(self, $$0):
        return self.obj.a($$0)

    def rl(self, $$0):
        return self.obj.rl($$0)

    def getExamples(self, ):
        return self.obj.getExamples()
