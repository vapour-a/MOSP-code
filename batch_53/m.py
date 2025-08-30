import jpype
import jpype.imports

# Auto-generated wrapper for m
class mWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = m(*args, **kwargs)

    def and(self, $$0):
        return self.obj.and($$0)

    def negate(self, ):
        return self.obj.negate()

    def or(self, $$0):
        return self.obj.or($$0)

    def test(self, paramChar):
        return self.obj.test(paramChar)
