import jpype
import jpype.imports

# Auto-generated wrapper for c
class cWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = c(*args, **kwargs)

    def create(self, paramsw, paramList, paramString, paramT):
        return self.obj.create(paramsw, paramList, paramString, paramT)
