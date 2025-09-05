import jpype
import jpype.imports

# Auto-generated wrapper for am
class amWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = am(*args, **kwargs)

    def a(self, ):
        return self.obj.a()

    def a(self, paramct):
        return self.obj.a(paramct)
