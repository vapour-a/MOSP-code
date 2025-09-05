import jpype
import jpype.imports

# Auto-generated wrapper for ewh
class ewhWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = ewh(*args, **kwargs)

    def acq(self, "minecraft", "alt"):
        return self.obj.acq("minecraft", "alt")

    def ewh(self, ):
        return self.obj.ewh()

    def a(self, ):
        return ewh.a()

    def a(self, $$0, $$1):
        return self.obj.a($$0, $$1)

    def StringBuilder(self, ):
        return self.obj.StringBuilder()

    def a(self, $$0):
        return self.obj.a($$0)
