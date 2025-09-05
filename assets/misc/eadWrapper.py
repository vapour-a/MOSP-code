import jpype
import jpype.imports

# Auto-generated wrapper for ead
class eadWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = ead(*args, **kwargs)

    def a(self, $$0, $$1):
        return ead.a($$0, $$1)

    def acq(self, $$0):
        return self.obj.acq($$0)

    def eag(self, $$1):
        return self.obj.eag($$1)

    def a(self, ):
        return ead.a()
