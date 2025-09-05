import jpype
import jpype.imports

# Auto-generated wrapper for czo
class czoWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = czo(*args, **kwargs)

    def tick(self, paramcmm, paramgu, paramdcb, paramT):
        return self.obj.tick(paramcmm, paramgu, paramdcb, paramT)
