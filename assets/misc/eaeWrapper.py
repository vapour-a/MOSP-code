import jpype
import jpype.imports

# Auto-generated wrapper for eae
class eaeWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = eae(*args, **kwargs)

    def a(self, paramFloat):
        return self.obj.a(paramFloat)

    def a(self, paramConsumer, paramdzk):
        return self.obj.a(paramConsumer, paramdzk)
