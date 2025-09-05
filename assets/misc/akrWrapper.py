import jpype
import jpype.imports

# Auto-generated wrapper for akr
class akrWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = akr(*args, **kwargs)

    def a(self, parama, paramakx, paramban1, paramban2, paramExecutor1, paramExecutor2):
        return self.obj.a(parama, paramakx, paramban1, paramban2, paramExecutor1, paramExecutor2)

    def c(self, ):
        return self.obj.c()

    def getClass(self, ):
        return self.obj.getClass()

    def a(self, param1T):
        return self.obj.a(param1T)
