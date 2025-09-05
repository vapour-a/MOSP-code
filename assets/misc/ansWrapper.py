import jpype
import jpype.imports

# Auto-generated wrapper for ans
class ansWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = ans(*args, **kwargs)

    def a(self, paramInt1, paramInt2):
        return self.obj.a(paramInt1, paramInt2)

    def b(self, paramInt1, paramInt2):
        return self.obj.b(paramInt1, paramInt2)

    def a(self, paramInt):
        return self.obj.a(paramInt)

    def a(self, ):
        return self.obj.a()

    def b(self, ):
        return self.obj.b()

    def c(self, ):
        return self.obj.c()

    def a(self, paramIntConsumer):
        return self.obj.a(paramIntConsumer)

    def a(self, paramArrayOfint):
        return self.obj.a(paramArrayOfint)

    def d(self, ):
        return self.obj.d()
