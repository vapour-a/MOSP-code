import jpype
import jpype.imports

# Auto-generated wrapper for fds
class fdsWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fds(*args, **kwargs)

    def c(self, ):
        return self.obj.c()
