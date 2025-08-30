import jpype
import jpype.imports

# Auto-generated wrapper for apv
class apvWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = apv(*args, **kwargs)

    def get(self, paramTimeUnit):
        return self.obj.get(paramTimeUnit)

    def get(self, $$0):
        return self.obj.get($$0)
