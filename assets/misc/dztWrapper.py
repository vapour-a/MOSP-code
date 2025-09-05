import jpype
import jpype.imports

# Auto-generated wrapper for dzt
class dztWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = dzt(*args, **kwargs)

    def a(self, paramJsonObject, paramT, paramJsonSerializationContext):
        return self.obj.a(paramJsonObject, paramT, paramJsonSerializationContext)

    def a(self, paramJsonObject, paramJsonDeserializationContext):
        return self.obj.a(paramJsonObject, paramJsonDeserializationContext)
