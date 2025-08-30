import jpype
import jpype.imports

# Auto-generated wrapper for bru
class bruWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = bru(*args, **kwargs)

    def gl(self, ):
        return self.obj.gl()
