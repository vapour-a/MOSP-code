import jpype
import jpype.imports

# Auto-generated wrapper for c
class cWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = c(*args, **kwargs)

    def consume(self, paramInt1, paramInt2, paramDouble):
        return self.obj.consume(paramInt1, paramInt2, paramDouble)
