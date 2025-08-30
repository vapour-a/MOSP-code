import jpype
import jpype.imports

# Auto-generated wrapper for eeu
class eeuWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = eeu(*args, **kwargs)

    def a(self, ):
        return self.obj.a()

    def a(self, parama):
        return self.obj.a(parama)

    def size(self, ):
        return self.obj.size()

    def merge(self, param1Int1, param1Int2, param1Int3):
        return self.obj.merge(param1Int1, param1Int2, param1Int3)
