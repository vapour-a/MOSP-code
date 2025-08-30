import jpype
import jpype.imports

# Auto-generated wrapper for fyl
class fylWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fyl(*args, **kwargs)

    def search(self, paramString):
        return self.obj.search(paramString)
