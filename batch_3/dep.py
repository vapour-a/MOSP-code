import jpype
import jpype.imports

# Auto-generated wrapper for dep
class depWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = dep(*args, **kwargs)

    def onResize(self, paramInt, paramT):
        return self.obj.onResize(paramInt, paramT)
