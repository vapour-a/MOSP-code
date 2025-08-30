import jpype
import jpype.imports

# Auto-generated wrapper for dap
class dapWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = dap(*args, **kwargs)

    def a(self, paramFloat):
        return self.obj.a(paramFloat)
