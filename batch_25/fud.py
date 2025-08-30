import jpype
import jpype.imports

# Auto-generated wrapper for fud
class fudWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fud(*args, **kwargs)

    def call(self, paramcfz, paramfew, parambfz, paramInt):
        return self.obj.call(paramcfz, paramfew, parambfz, paramInt)
