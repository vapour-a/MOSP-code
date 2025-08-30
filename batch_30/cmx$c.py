import jpype
import jpype.imports

# Auto-generated wrapper for c
class cWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = c(*args, **kwargs)

    def test(self, parambfn, paramgu, paramddx):
        return self.obj.test(parambfn, paramgu, paramddx)
