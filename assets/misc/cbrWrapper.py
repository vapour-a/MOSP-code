import jpype
import jpype.imports

# Auto-generated wrapper for cbr
class cbrWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = cbr(*args, **kwargs)

    def a(self, paramcbf, paramInt, paramcfz):
        return self.obj.a(paramcbf, paramInt, paramcfz)

    def a(self, paramcbf, paramInt1, paramInt2):
        return self.obj.a(paramcbf, paramInt1, paramInt2)
