import jpype
import jpype.imports

# Auto-generated wrapper for ehj
class ehjWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = ehj(*args, **kwargs)

    def createMonitor(self, paramLong):
        return self.obj.createMonitor(paramLong)
