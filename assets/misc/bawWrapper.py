import jpype
import jpype.imports

# Auto-generated wrapper for baw
class bawWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = baw(*args, **kwargs)

    def finish(self, ):
        return self.obj.finish()
