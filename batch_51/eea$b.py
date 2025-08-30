import jpype
import jpype.imports

# Auto-generated wrapper for b
class bWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = b(*args, **kwargs)

    def compile(self, paramFileSystem, paramString):
        return self.obj.compile(paramFileSystem, paramString)
