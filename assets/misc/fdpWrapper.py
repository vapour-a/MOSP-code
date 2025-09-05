import jpype
import jpype.imports

# Auto-generated wrapper for fdp
class fdpWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fdp(*args, **kwargs)

    def a(self, paramBoolean):
        return self.obj.a(paramBoolean)
