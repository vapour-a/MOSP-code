import jpype
import jpype.imports

# Auto-generated wrapper for aio
class aioWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = aio(*args, **kwargs)

    def a(self, paramclt):
        return self.obj.a(paramclt)

    def a(self, paramclt, paramdec):
        return self.obj.a(paramclt, paramdec)

    def a(self, ):
        return self.obj.a()

    def b(self, ):
        return self.obj.b()
