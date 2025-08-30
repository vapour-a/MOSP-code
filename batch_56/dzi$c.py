import jpype
import jpype.imports

# Auto-generated wrapper for c
class cWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = c(*args, **kwargs)

    def deserialize(self, $$0, $$1, $$2):
        return self.obj.deserialize($$0, $$1, $$2)

    def acq(self, $$4):
        return self.obj.acq($$4)

    def JsonSyntaxException(self, "'"):
        return self.obj.JsonSyntaxException("'")

    def UnsupportedOperationException(self, deserialized"):
        return self.obj.UnsupportedOperationException(deserialized")

    def serialize(self, $$0, $$1, $$2):
        return self.obj.serialize($$0, $$1, $$2)

    def JsonSyntaxException(self, $$0):
        return self.obj.JsonSyntaxException($$0)

    def JsonObject(self, ):
        return self.obj.JsonObject()
