import jpype
import jpype.imports

# Auto-generated wrapper for a
class aWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = a(*args, **kwargs)

    def deserialize(self, paramJsonObject):
        return self.obj.deserialize(paramJsonObject)
