import jpype
import jpype.imports

# Auto-generated wrapper for b
class bWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = b(*args, **kwargs)

    def shouldGenerate(self, paramLong, paramInt1, paramInt2, paramInt3, paramFloat):
        return self.obj.shouldGenerate(paramLong, paramInt1, paramInt2, paramInt3, paramFloat)
