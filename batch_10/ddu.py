import jpype
import jpype.imports

# Auto-generated wrapper for ddu
class dduWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = ddu(*args, **kwargs)

    def a(self, paramInt):
        return self.obj.a(paramInt)

    def a(self, paramInt, paramdcb):
        return self.obj.a(paramInt, paramdcb)
