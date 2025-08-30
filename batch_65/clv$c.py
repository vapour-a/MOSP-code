import jpype
import jpype.imports

# Auto-generated wrapper for c
class cWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = c(*args, **kwargs)

    def get(self, paramdcb, paramcls, paramgu, parameen):
        return self.obj.get(paramdcb, paramcls, paramgu, parameen)
