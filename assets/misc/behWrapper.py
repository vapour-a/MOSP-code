import jpype
import jpype.imports

# Auto-generated wrapper for beh
class behWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = beh(*args, **kwargs)

    def a(self, paramdcb, paramcmn, paramgu):
        return self.obj.a(paramdcb, paramcmn, paramgu)
