import jpype
import jpype.imports

# Auto-generated wrapper for j
class jWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = j(*args, **kwargs)

    def a(self, ):
        return self.obj.a()

    def c(self, ):
        return self.obj.c()
