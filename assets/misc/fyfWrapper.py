import jpype
import jpype.imports

# Auto-generated wrapper for fyf
class fyfWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fyf(*args, **kwargs)

    def fyf(self, $$0, $$1, $$2):
        return self.obj.fyf($$0, $$1, $$2)

    def computeNext(self, ):
        return self.obj.computeNext()
