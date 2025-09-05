import jpype
import jpype.imports

# Auto-generated wrapper for bjo
class bjoWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = bjo(*args, **kwargs)

    def a(self, $$0):
        return bjo.a($$0)

    def Long2LongOpenHashMap(self, ):
        return self.obj.Long2LongOpenHashMap()

    def MutableLong(self, 0L):
        return self.obj.MutableLong(0L)
