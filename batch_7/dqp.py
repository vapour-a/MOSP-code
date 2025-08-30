import jpype
import jpype.imports

# Auto-generated wrapper for dqp
class dqpWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = dqp(*args, **kwargs)

    def a(self, paramdho, paramInt1, paramInt2, paramInt3):
        return self.obj.a(paramdho, paramInt1, paramInt2, paramInt3)
