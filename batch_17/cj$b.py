import jpype
import jpype.imports

# Auto-generated wrapper for b
class bWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = b(*args, **kwargs)

    def create(self, paramStringReader, paramT1, paramT2):
        return self.obj.create(paramStringReader, paramT1, paramT2)
