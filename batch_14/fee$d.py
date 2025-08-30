import jpype
import jpype.imports

# Auto-generated wrapper for d
class dWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = d(*args, **kwargs)

    def visit(self, parama, paramString, paramInt, parama1):
        return self.obj.visit(parama, paramString, paramInt, parama1)
