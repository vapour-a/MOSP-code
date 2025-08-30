import jpype
import jpype.imports

# Auto-generated wrapper for sr
class srWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = sr(*args, **kwargs)

    def decorate(self, paramaig, paramsw):
        return self.obj.decorate(paramaig, paramsw)
