import jpype
import jpype.imports

# Auto-generated wrapper for blg
class blgWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = blg(*args, **kwargs)

    def trigger(self, paramaif, paramE, paramLong):
        return self.obj.trigger(paramaif, paramE, paramLong)
