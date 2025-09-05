import jpype
import jpype.imports

# Auto-generated wrapper for ecz
class eczWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = ecz(*args, **kwargs)

    def a(self, $$0, $$1):
        return ecz.a($$0, $$1)

    def acq(self, $$0):
        return self.obj.acq($$0)

    def ecx(self, $$1):
        return self.obj.ecx($$1)

    def a(self, ):
        return ecz.a()
