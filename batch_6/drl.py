import jpype
import jpype.imports

# Auto-generated wrapper for drl
class drlWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = drl(*args, **kwargs)

    def a(self, paramapf, paramgu):
        return self.obj.a(paramapf, paramgu)

    def a_(self, $$0, $$1, $$2):
        return self.obj.a_($$0, $$1, $$2)
