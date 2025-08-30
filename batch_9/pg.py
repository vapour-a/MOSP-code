import jpype
import jpype.imports

# Auto-generated wrapper for pg
class pgWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = pg(*args, **kwargs)

    def a(self, ):
        return self.obj.a()
