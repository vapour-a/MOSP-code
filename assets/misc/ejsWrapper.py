import jpype
import jpype.imports

# Auto-generated wrapper for ejs
class ejsWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = ejs(*args, **kwargs)

    def a(self, $$0):
        return ejs.a($$0)

    def ejs(self, ):
        return self.obj.ejs()

    def JsonParser(self, ):
        return self.obj.JsonParser()
