import jpype
import jpype.imports

# Auto-generated wrapper for d
class dWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = d(*args, **kwargs)

    def constant(self, $$0):
        return d.constant($$0)

    def get(self, paramFloat):
        return self.obj.get(paramFloat)
