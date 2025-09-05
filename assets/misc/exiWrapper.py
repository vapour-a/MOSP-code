import jpype
import jpype.imports

# Auto-generated wrapper for exi
class exiWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = exi(*args, **kwargs)

    def a(self, paramInt1, paramInt2, paramInt3, paramInt4, paramInt5, paramInt6):
        return self.obj.a(paramInt1, paramInt2, paramInt3, paramInt4, paramInt5, paramInt6)
