import jpype
import jpype.imports

# Auto-generated wrapper for dvn
class dvnWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = dvn(*args, **kwargs)

    def a(self, paramdcb, paramapf):
        return self.obj.a(paramdcb, paramapf)

    def a(self, ):
        return self.obj.a()
