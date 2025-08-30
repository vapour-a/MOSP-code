import jpype
import jpype.imports

# Auto-generated wrapper for d
class dWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = d(*args, **kwargs)

    def load(self, paramT, paramInt1, paramInt2):
        return self.obj.load(paramT, paramInt1, paramInt2)
