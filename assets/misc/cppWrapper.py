import jpype
import jpype.imports

# Auto-generated wrapper for cpp
class cppWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = cpp(*args, **kwargs)

    def a(self, paramcmp, paramgu, paramdcb, paramBoolean):
        return self.obj.a(paramcmp, paramgu, paramdcb, paramBoolean)

    def a(self, paramcmm, paramapf, paramgu, paramdcb):
        return self.obj.a(paramcmm, paramapf, paramgu, paramdcb)

    def a(self, paramaif, paramapf, paramgu, paramdcb):
        return self.obj.a(paramaif, paramapf, paramgu, paramdcb)
