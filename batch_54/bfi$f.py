import jpype
import jpype.imports

# Auto-generated wrapper for f
class fWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = f(*args, **kwargs)

    def constant(self, $$0):
        return f.constant($$0)

    def get(self, paramFloat):
        return self.obj.get(paramFloat)
