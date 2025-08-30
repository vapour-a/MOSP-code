import jpype
import jpype.imports

# Auto-generated wrapper for f
class fWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = f(*args, **kwargs)

    def test(self, paramdcb, paramcls, paramgu):
        return self.obj.test(paramdcb, paramcls, paramgu)
