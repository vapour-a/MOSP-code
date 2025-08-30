import jpype
import jpype.imports

# Auto-generated wrapper for b
class bWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = b(*args, **kwargs)

    def consume(self, paramInt1, paramInt2, paramInt3, paramDouble):
        return self.obj.consume(paramInt1, paramInt2, paramInt3, paramDouble)
