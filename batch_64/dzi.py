import jpype
import jpype.imports

# Auto-generated wrapper for dzi
class dziWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = dzi(*args, **kwargs)

    def a(self, $$0, $$1):
        return self.obj.a($$0, $$1)

    def a(self, $$0):
        return self.obj.a($$0)

    def a(self, ):
        return self.obj.a()

    def a(self, $$0, $$1, $$2, Function<E, $$3):
        return self.obj.a($$0, $$1, $$2, Function<E, $$3)

    def a(self, param1T, param1JsonSerializationContext):
        return self.obj.a(param1T, param1JsonSerializationContext)

    def a(self, param1JsonElement, param1JsonDeserializationContext):
        return self.obj.a(param1JsonElement, param1JsonDeserializationContext)

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
