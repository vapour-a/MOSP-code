import jpype
import jpype.imports

# Auto-generated wrapper for fuh
class fuhWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fuh(*args, **kwargs)

    def a(self, paramacq, paramPath):
        return self.obj.a(paramacq, paramPath)
