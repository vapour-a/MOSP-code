import jpype
import jpype.imports

# Auto-generated wrapper for ajx
class ajxWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = ajx(*args, **kwargs)

    def a(self, ):
        return self.obj.a()

    def a(self, paramJsonObject):
        return self.obj.a(paramJsonObject)
