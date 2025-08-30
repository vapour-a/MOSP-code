import jpype
import jpype.imports

# Auto-generated wrapper for ewt
class ewtWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = ewt(*args, **kwargs)

    def C(self, ):
        return self.obj.C()
