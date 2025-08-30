import jpype
import jpype.imports

# Auto-generated wrapper for asr
class asrWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = asr(*args, **kwargs)

    def asr(self, $$0, $$1):
        return self.obj.asr($$0, $$1)

    def makeRule(self, ):
        return self.obj.makeRule()

    def fixTypeEverywhere(self, "EntityMinecartIdentifiersFix", (Type):
        return self.obj.fixTypeEverywhere("EntityMinecartIdentifiersFix", (Type)
