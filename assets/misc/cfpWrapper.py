import jpype
import jpype.imports

# Auto-generated wrapper for cfp
class cfpWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = cfp(*args, **kwargs)

    def cfp(self, $$0, $$1, $$2):
        return self.obj.cfp($$0, $$1, $$2)

    def h(self, ):
        return self.obj.h()

    def acq(self, this.c):
        return self.obj.acq(this.c)

    def i(self, ):
        return self.obj.i()
