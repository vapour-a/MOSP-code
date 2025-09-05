import jpype
import jpype.imports

# Auto-generated wrapper for clx
class clxWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = clx(*args, **kwargs)

    def getColor(self, paramcnk, paramDouble1, paramDouble2):
        return self.obj.getColor(paramcnk, paramDouble1, paramDouble2)
