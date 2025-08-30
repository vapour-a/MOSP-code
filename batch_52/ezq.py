import jpype
import jpype.imports

# Auto-generated wrapper for ezq
class ezqWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = ezq(*args, **kwargs)

    def a(self, ):
        return self.obj.a()

    def b(self, ):
        return self.obj.b()
