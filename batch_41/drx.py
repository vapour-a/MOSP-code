import jpype
import jpype.imports

# Auto-generated wrapper for drx
class drxWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = drx(*args, **kwargs)

    def afterPlace(self, paramcng, paramcne, paramddy, paramapf, paramdrs, paramclt, paramdsp):
        return self.obj.afterPlace(paramcng, paramcne, paramddy, paramapf, paramdrs, paramclt, paramdsp)
