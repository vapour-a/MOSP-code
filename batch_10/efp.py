import jpype
import jpype.imports

# Auto-generated wrapper for efp
class efpWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = efp(*args, **kwargs)

    def b(self, paramgu, paramT):
        return self.obj.b(paramgu, paramT)
