import jpype
import jpype.imports

# Auto-generated wrapper for fxi
class fxiWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fxi(*args, **kwargs)

    def a(self, ):
        return self.obj.a()
