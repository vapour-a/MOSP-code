import jpype
import jpype.imports

# Auto-generated wrapper for ekc
class ekcWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = ekc(*args, **kwargs)

    def a(self, $$0):
        return ekc.a($$0)

    def ekc(self, ):
        return self.obj.ekc()

    def JsonParser(self, ):
        return self.obj.JsonParser()
