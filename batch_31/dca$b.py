import jpype
import jpype.imports

# Auto-generated wrapper for b
class bWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = b(*args, **kwargs)

    def evaluate(self, paramdcb, paramcls, paramgu):
        return self.obj.evaluate(paramdcb, paramcls, paramgu)
