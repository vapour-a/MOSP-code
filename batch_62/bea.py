import jpype
import jpype.imports

# Auto-generated wrapper for bea
class beaWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = bea(*args, **kwargs)

    def H_(self, ):
        return self.obj.H_()
