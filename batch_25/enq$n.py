import jpype
import jpype.imports

# Auto-generated wrapper for n
class nWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = n(*args, **kwargs)

    def a(self, paraml, paramenr, paramInt1, paramInt2, paramInt3, paramConsumer):
        return self.obj.a(paraml, paramenr, paramInt1, paramInt2, paramInt3, paramConsumer)

    def a(self, paramT):
        return self.obj.a(paramT)

    def f(self, ):
        return self.obj.f()
