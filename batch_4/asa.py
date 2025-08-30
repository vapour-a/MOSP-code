import jpype
import jpype.imports

# Auto-generated wrapper for asa
class asaWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = asa(*args, **kwargs)

    def asa(self, $$0):
        return self.obj.asa($$0)

    def makeRule(self, ):
        return self.obj.makeRule()

    def convertUnchecked(self, "DecoratedPotFieldRenameFix", $$0, $$1):
        return self.obj.convertUnchecked("DecoratedPotFieldRenameFix", $$0, $$1)
