import jpype
import jpype.imports

# Auto-generated wrapper for ejk
class ejkWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = ejk(*args, **kwargs)

    def a(self, $$0):
        return ejk.a($$0)

    def ejk(self, ):
        return self.obj.ejk()

    def JsonParser(self, ):
        return self.obj.JsonParser()
