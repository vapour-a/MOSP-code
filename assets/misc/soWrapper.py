import jpype
import jpype.imports

# Auto-generated wrapper for so
class soWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = so(*args, **kwargs)

    def c(self, ):
        return self.obj.c()
