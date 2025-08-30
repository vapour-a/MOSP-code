import jpype
import jpype.imports

# Auto-generated wrapper for bgw
class bgwWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = bgw(*args, **kwargs)

    def j(self, ):
        return self.obj.j()
