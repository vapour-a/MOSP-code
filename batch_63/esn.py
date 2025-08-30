import jpype
import jpype.imports

# Auto-generated wrapper for esn
class esnWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = esn(*args, **kwargs)

    def q(self, ):
        return self.obj.q()

    def aD_(self, ):
        return self.obj.aD_()

    def a(self, ):
        return self.obj.a()
