import jpype
import jpype.imports

# Auto-generated wrapper for fdc
class fdcWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fdc(*args, **kwargs)

    def fdc(self, ):
        return self.obj.fdc()

    def a(self, paramFloat1, paramFloat2, paramFloat3):
        return self.obj.a(paramFloat1, paramFloat2, paramFloat3)
