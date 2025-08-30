import jpype
import jpype.imports

# Auto-generated wrapper for f
class fWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = f(*args, **kwargs)

    def getWidth(self, paramInt, paramts):
        return self.obj.getWidth(paramInt, paramts)
