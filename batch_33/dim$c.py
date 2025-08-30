import jpype
import jpype.imports

# Auto-generated wrapper for c
class cWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = c(*args, **kwargs)

    def getDistance(self, paramDouble1, paramDouble2, paramDouble3):
        return self.obj.getDistance(paramDouble1, paramDouble2, paramDouble3)
