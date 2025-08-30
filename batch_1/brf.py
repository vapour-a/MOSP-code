import jpype
import jpype.imports

# Auto-generated wrapper for brf
class brfWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = brf(*args, **kwargs)

    def brf(self, $$0, $$1):
        return self.obj.brf($$0, $$1)

    def a(self, $$0):
        return self.obj.a($$0)
