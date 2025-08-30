import jpype
import jpype.imports

# Auto-generated wrapper for h
class hWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = h(*args, **kwargs)

    def call(self, paramc, parame, paramf):
        return self.obj.call(paramc, parame, paramf)
