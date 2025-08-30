import jpype
import jpype.imports

# Auto-generated wrapper for d
class dWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = d(*args, **kwargs)

    def test(self, paramcls, paramgu, paramc):
        return self.obj.test(paramcls, paramgu, paramc)
