import jpype
import jpype.imports

# Auto-generated wrapper for h
class hWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = h(*args, **kwargs)

    def accept(self, paramInt, paramf):
        return self.obj.accept(paramInt, paramf)
