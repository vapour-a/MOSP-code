import jpype
import jpype.imports

# Auto-generated wrapper for emv
class emvWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = emv(*args, **kwargs)

    def emv(self, $$0, $$1, $$2):
        return self.obj.emv($$0, $$1, $$2)

    def run(self, ):
        return self.obj.run()
