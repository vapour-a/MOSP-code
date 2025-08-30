import jpype
import jpype.imports

# Auto-generated wrapper for asp
class aspWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = asp(*args, **kwargs)

    def asp(self, $$0, $$1):
        return self.obj.asp($$0, $$1)

    def makeRule(self, ):
        return self.obj.makeRule()
