import jpype
import jpype.imports

# Auto-generated wrapper for dfl
class dflWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = dfl(*args, **kwargs)

    def toString(self, ):
        return self.obj.toString()

    def hashCode(self, ):
        return self.obj.hashCode()

    def dfl(self, $$0, $$1):
        return self.obj.dfl($$0, $$1)

    def equals(self, $$0):
        return self.obj.equals($$0)

    def a(self, ):
        return self.obj.a()

    def b(self, ):
        return self.obj.b()

    def acq(self, "overworld"):
        return self.obj.acq("overworld")

    def acq(self, "the_nether"):
        return self.obj.acq("the_nether")

    def acq(self, "the_end"):
        return self.obj.acq("the_end")
