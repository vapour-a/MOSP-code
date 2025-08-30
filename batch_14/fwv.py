import jpype
import jpype.imports

# Auto-generated wrapper for fwv
class fwvWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fwv(*args, **kwargs)

    def a(self, paramacq):
        return self.obj.a(paramacq)

    def a(self, paramacq, paramfwz):
        return self.obj.a(paramacq, paramfwz)
