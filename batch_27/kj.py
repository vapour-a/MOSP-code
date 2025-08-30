import jpype
import jpype.imports

# Auto-generated wrapper for kj
class kjWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = kj(*args, **kwargs)

    def generate(self, BiConsumer<acq, $$0):
        return self.obj.generate(BiConsumer<acq, $$0)

    def a(self, ):
        return self.obj.a()
