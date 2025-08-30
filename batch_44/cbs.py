import jpype
import jpype.imports

# Auto-generated wrapper for cbs
class cbsWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = cbs(*args, **kwargs)

    def a(self, paramcbf, paramhn, paramcfz, paramArrayOfint):
        return self.obj.a(paramcbf, paramhn, paramcfz, paramArrayOfint)

    def a(self, paramcbf, paramInt, paramcfz):
        return self.obj.a(paramcbf, paramInt, paramcfz)

    def a(self, paramcbf, paramcfz):
        return self.obj.a(paramcbf, paramcfz)

    def a(self, paramcbf, paramInt1, paramInt2):
        return self.obj.a(paramcbf, paramInt1, paramInt2)
