import jpype
import jpype.imports

# Auto-generated wrapper for eor
class eorWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = eor(*args, **kwargs)

    def getColor(self, paramcfz, paramInt):
        return self.obj.getColor(paramcfz, paramInt)
