import jpype
import jpype.imports

# Auto-generated wrapper for ekh
class ekhWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = ekh(*args, **kwargs)

    def a(self, $$0):
        return ekh.a($$0)

    def ekh(self, ):
        return self.obj.ekh()
