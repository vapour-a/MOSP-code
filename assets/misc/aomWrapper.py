import jpype
import jpype.imports

# Auto-generated wrapper for aom
class aomWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = aom(*args, **kwargs)

    def codepoint(self, $$0, $$1):
        return aom.codepoint($$0, $$1)

    def forward(self, $$0, $$1):
        return aom.forward($$0, $$1)

    def forward(self, $$0, $$1, $$2):
        return aom.forward($$0, $$1, $$2)

    def backward(self, $$0, $$1):
        return aom.backward($$0, $$1)

    def backward(self, $$0, $$1, $$2):
        return aom.backward($$0, $$1, $$2)

    def decorateOutput(self, $$0, $$1):
        return aom.decorateOutput($$0, $$1)

    def composite(self, ):
        return aom.composite()

    def composite(self, $$0):
        return aom.composite($$0)

    def composite(self, $$0, $$1):
        return aom.composite($$0, $$1)

    def fromPair(self, $$0, $$1):
        return self.obj.fromPair($$0, $$1)

    def composite(self, $$0):
        return aom.composite($$0)

    def fromList(self, (List<aom>):
        return self.obj.fromList((List<aom>)

    def composite(self, $$0):
        return aom.composite($$0)

    def fromPair(self, $$0.get(0):
        return self.obj.fromPair($$0.get(0)

    def fromList(self, (List<aom>):
        return self.obj.fromList((List<aom>)

    def fromPair(self, $$0, $$1):
        return aom.fromPair($$0, $$1)

    def fromList(self, $$0):
        return aom.fromList($$0)

    def accept(self, paramaon):
        return self.obj.accept(paramaon)
