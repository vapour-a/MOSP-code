import jpype
import jpype.imports

# Auto-generated wrapper for emw
class emwWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = emw(*args, **kwargs)

    def emw(self, $$0, $$1, $$2, $$3):
        return self.obj.emw($$0, $$1, $$2, $$3)

    def run(self, ):
        return self.obj.run()
