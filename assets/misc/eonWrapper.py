import jpype
import jpype.imports

# Auto-generated wrapper for eon
class eonWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = eon(*args, **kwargs)

    def getColor(self, paramdcb, paramclp, paramgu, paramInt):
        return self.obj.getColor(paramdcb, paramclp, paramgu, paramInt)
