import jpype
import jpype.imports

# Auto-generated wrapper for beg
class begWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = beg(*args, **kwargs)

    def a(self, paramha):
        return self.obj.a(paramha)

    def a(self, paramInt, paramcfz, paramha):
        return self.obj.a(paramInt, paramcfz, paramha)

    def b(self, paramInt, paramcfz, paramha):
        return self.obj.b(paramInt, paramcfz, paramha)
