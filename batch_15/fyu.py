import jpype
import jpype.imports

# Auto-generated wrapper for fyu
class fyuWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fyu(*args, **kwargs)

    def a(self, ):
        return self.obj.a()

    def a(self, paramInt):
        return self.obj.a(paramInt)
