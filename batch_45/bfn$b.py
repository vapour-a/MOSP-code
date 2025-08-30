import jpype
import jpype.imports

# Auto-generated wrapper for b
class bWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = b(*args, **kwargs)

    def create(self, parambfn, paramcmm):
        return self.obj.create(parambfn, paramcmm)
