import jpype
import jpype.imports

# Auto-generated wrapper for aip
class aipWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = aip(*args, **kwargs)

    def create(self, paramInt):
        return self.obj.create(paramInt)
