import jpype
import jpype.imports

# Auto-generated wrapper for b
class bWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = b(*args, **kwargs)

    def setupBufferState(self, paramInt1, paramInt2, paramInt3, paramLong, paramInt4, paramInt5):
        return self.obj.setupBufferState(paramInt1, paramInt2, paramInt3, paramLong, paramInt4, paramInt5)
