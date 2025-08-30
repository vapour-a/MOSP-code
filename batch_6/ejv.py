import jpype
import jpype.imports

# Auto-generated wrapper for ejv
class ejvWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = ejv(*args, **kwargs)

    def a(self, $$0):
        return ejv.a($$0)

    def ejv(self, ):
        return self.obj.ejv()

    def JsonParser(self, ):
        return self.obj.JsonParser()
