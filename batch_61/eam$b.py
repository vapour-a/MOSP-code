import jpype
import jpype.imports

# Auto-generated wrapper for b
class bWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = b(*args, **kwargs)

    def a(self, paramapf, paramInt1, paramInt2):
        return self.obj.a(paramapf, paramInt1, paramInt2)

    def a(self, paramJsonObject, paramJsonSerializationContext):
        return self.obj.a(paramJsonObject, paramJsonSerializationContext)

    def a(self, ):
        return self.obj.a()
