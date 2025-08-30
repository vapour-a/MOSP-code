import jpype
import jpype.imports

# Auto-generated wrapper for dfi
class dfiWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = dfi(*args, **kwargs)

    def acq(self, "overworld"):
        return self.obj.acq("overworld")

    def acq(self, "the_nether"):
        return self.obj.acq("the_nether")

    def acq(self, "the_end"):
        return self.obj.acq("the_end")

    def a(self, $$0):
        return dfi.a($$0)

    def acq(self, $$0):
        return self.obj.acq($$0)
