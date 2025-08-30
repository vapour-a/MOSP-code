import jpype
import jpype.imports

# Auto-generated wrapper for kd
class kdWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = kd(*args, **kwargs)

    def generate(self, BiConsumer<acq, paramBiConsumer):
        return self.obj.generate(BiConsumer<acq, paramBiConsumer)
