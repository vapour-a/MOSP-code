import jpype
import jpype.imports

# Auto-generated wrapper for ap
class apWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = ap(*args, **kwargs)

    def createRequirements(self, paramCollection):
        return self.obj.createRequirements(paramCollection)
