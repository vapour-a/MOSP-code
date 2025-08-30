import jpype
import jpype.imports

# Auto-generated wrapper for c
class cWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = c(*args, **kwargs)

    def encode(self, paramGameProfile, paramString):
        return self.obj.encode(paramGameProfile, paramString)
