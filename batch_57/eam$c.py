import jpype
import jpype.imports

# Auto-generated wrapper for c
class cWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = c(*args, **kwargs)

    def deserialize(self, paramJsonObject, paramJsonDeserializationContext):
        return self.obj.deserialize(paramJsonObject, paramJsonDeserializationContext)
