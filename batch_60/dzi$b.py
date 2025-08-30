import jpype
import jpype.imports

# Auto-generated wrapper for b
class bWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = b(*args, **kwargs)

    def a(self, paramT, paramJsonSerializationContext):
        return self.obj.a(paramT, paramJsonSerializationContext)

    def a(self, paramJsonElement, paramJsonDeserializationContext):
        return self.obj.a(paramJsonElement, paramJsonDeserializationContext)
