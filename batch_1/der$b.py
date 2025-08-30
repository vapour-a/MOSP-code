import jpype
import jpype.imports

# Auto-generated wrapper for b
class bWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = b(*args, **kwargs)

    def read(self, paramhj, paramd, parama):
        return self.obj.read(paramhj, paramd, parama)
