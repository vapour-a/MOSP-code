import jpype
import jpype.imports

# Auto-generated wrapper for ejg
class ejgWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = ejg(*args, **kwargs)

    def a(self, $$0):
        return ejg.a($$0)

    def JsonParser(self, ):
        return self.obj.JsonParser()

    def ejg(self, ):
        return self.obj.ejg()
