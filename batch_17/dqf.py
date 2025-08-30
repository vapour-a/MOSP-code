import jpype
import jpype.imports

# Auto-generated wrapper for dqf
class dqfWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = dqf(*args, **kwargs)

    def dqf(self, $$0, $$1, $$2):
        return self.obj.dqf($$0, $$1, $$2)

    def a(self, $$0, $$1, $$2):
        return dqf.a($$0, $$1, $$2)

    def dqf(self, $$0, $$1, $$2):
        return self.obj.dqf($$0, $$1, $$2)

    def a(self, $$0, $$1):
        return self.obj.a($$0, $$1)

    def a(self, ):
        return self.obj.a()

    def toString(self, ):
        return self.obj.toString()
