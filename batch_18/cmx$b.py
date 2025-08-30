import jpype
import jpype.imports

# Auto-generated wrapper for b
class bWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = b(*args, **kwargs)

    def query(self, paramLong, paramConsumer):
        return self.obj.query(paramLong, paramConsumer)
