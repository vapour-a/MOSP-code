import jpype
import jpype.imports

# Auto-generated wrapper for eem
class eemWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = eem(*args, **kwargs)

    def apply(self, paramBoolean1, paramBoolean2):
        return self.obj.apply(paramBoolean1, paramBoolean2)
