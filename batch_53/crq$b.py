import jpype
import jpype.imports

# Auto-generated wrapper for b
class bWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = b(*args, **kwargs)

    def a(self, paramS1, paramS2):
        return self.obj.a(paramS1, paramS2)

    def a(self, paramS):
        return self.obj.a(paramS)

    def b(self, ):
        return self.obj.b()
