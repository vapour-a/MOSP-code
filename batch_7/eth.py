import jpype
import jpype.imports

# Auto-generated wrapper for eth
class ethWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = eth(*args, **kwargs)

    def eth(self, $$0, $$1):
        return self.obj.eth($$0, $$1)
