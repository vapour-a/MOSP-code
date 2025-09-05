import jpype
import jpype.imports

# Auto-generated wrapper for drg
class drgWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = drg(*args, **kwargs)

    def a_(self, $$0, $$1, $$2):
        return self.obj.a_($$0, $$1, $$2)

    def a(self, paramdrf, paramapf, paramgu):
        return self.obj.a(paramdrf, paramapf, paramgu)
