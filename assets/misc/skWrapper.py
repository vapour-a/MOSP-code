import jpype
import jpype.imports

# Auto-generated wrapper for sk
class skWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = sk(*args, **kwargs)

    def a(self, paramsw):
        return self.obj.a(paramsw)

    def a(self, ):
        return self.obj.a()

    def b(self, ):
        return self.obj.b()
