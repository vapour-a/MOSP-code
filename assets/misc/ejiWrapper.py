import jpype
import jpype.imports

# Auto-generated wrapper for eji
class ejiWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = eji(*args, **kwargs)

    def a(self, $$0):
        return eji.a($$0)

    def eji(self, ):
        return self.obj.eji()

    def JsonParser(self, ):
        return self.obj.JsonParser()
