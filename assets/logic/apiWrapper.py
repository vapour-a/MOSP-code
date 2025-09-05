import jpype
import jpype.imports

# Auto-generated wrapper for api
class apiWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = api(*args, **kwargs)

    def update(self, parama):
        return self.obj.update(parama)

    def update(self, param1ArrayOfbyte):
        return self.obj.update(param1ArrayOfbyte)
