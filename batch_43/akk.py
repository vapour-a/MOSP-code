import jpype
import jpype.imports

# Auto-generated wrapper for akk
class akkWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = akk(*args, **kwargs)

    def a(self, paramConsumer):
        return self.obj.a(paramConsumer)
