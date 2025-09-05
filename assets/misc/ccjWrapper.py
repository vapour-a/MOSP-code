import jpype
import jpype.imports

# Auto-generated wrapper for ccj
class ccjWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = ccj(*args, **kwargs)

    def createMenu(self, paramInt, parambyn, parambyo):
        return self.obj.createMenu(paramInt, parambyn, parambyo)
