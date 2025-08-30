import jpype
import jpype.imports

# Auto-generated wrapper for c
class cWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = c(*args, **kwargs)

    def a(self, paramInt, paramString):
        return self.obj.a(paramInt, paramString)

    def a(self, paramInt1, paramString, paramInt2):
        return self.obj.a(paramInt1, paramString, paramInt2)

    def b(self, paramInt, paramString):
        return self.obj.b(paramInt, paramString)

    def a(self, paramInt1, paramacq, paramInt2):
        return self.obj.a(paramInt1, paramacq, paramInt2)
