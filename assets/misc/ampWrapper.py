import jpype
import jpype.imports

# Auto-generated wrapper for amp
class ampWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = amp(*args, **kwargs)

    def DecimalFormat(self, "########0.00"):
        return self.obj.DecimalFormat("########0.00")

    def format(self, paramInt):
        return self.obj.format(paramInt)
