import jpype
import jpype.imports

# Auto-generated wrapper for d
class dWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = d(*args, **kwargs)

    def accept(self, paramts, paramInt1, paramInt2):
        return self.obj.accept(paramts, paramInt1, paramInt2)
