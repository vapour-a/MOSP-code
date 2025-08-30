import jpype
import jpype.imports

# Auto-generated wrapper for dwb
class dwbWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = dwb(*args, **kwargs)

    def a(self, paramapf, paramqr):
        return self.obj.a(paramapf, paramqr)

    def a(self, ):
        return self.obj.a()
