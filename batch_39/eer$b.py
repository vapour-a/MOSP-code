import jpype
import jpype.imports

# Auto-generated wrapper for b
class bWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = b(*args, **kwargs)

    def consume(self, paramInt1, paramInt2, paramInt3, paramInt4, paramInt5, paramInt6):
        return self.obj.consume(paramInt1, paramInt2, paramInt3, paramInt4, paramInt5, paramInt6)
