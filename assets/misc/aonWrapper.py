import jpype
import jpype.imports

# Auto-generated wrapper for aon
class aonWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = aon(*args, **kwargs)

    def accept(self, paramInt1, paramts, paramInt2):
        return self.obj.accept(paramInt1, paramts, paramInt2)
