import jpype
import jpype.imports

# Auto-generated wrapper for r
class rWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = r(*args, **kwargs)

    def toString(self, ):
        return self.obj.toString()

    def a(self, ):
        return self.obj.a()

    def hashCode(self, ):
        return self.obj.hashCode()

    def equals(self, $$0):
        return self.obj.equals($$0)

    def tryApply(self, $$0, $$1, $$2):
        return self.obj.tryApply($$0, $$1, $$2)
