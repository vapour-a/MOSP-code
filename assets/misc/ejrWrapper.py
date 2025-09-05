import jpype
import jpype.imports

# Auto-generated wrapper for ejr
class ejrWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = ejr(*args, **kwargs)

    def a(self, $$0):
        return ejr.a($$0)

    def JsonParser(self, ):
        return self.obj.JsonParser()

    def ejr(self, ):
        return self.obj.ejr()
