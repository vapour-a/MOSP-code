import jpype
import jpype.imports

# Auto-generated wrapper for jg
class jgWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = jg(*args, **kwargs)

    def writeIfNeeded(self, paramPath, paramArrayOfbyte, paramHashCode):
        return self.obj.writeIfNeeded(paramPath, paramArrayOfbyte, paramHashCode)
