import jpype
import jpype.imports

# Auto-generated wrapper for egt
class egtWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = egt(*args, **kwargs)

    def execute(self, ):
        return self.obj.execute()
