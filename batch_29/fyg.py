import jpype
import jpype.imports

# Auto-generated wrapper for fyg
class fygWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = fyg(*args, **kwargs)

    def fyg(self, $$0, $$1, $$2):
        return self.obj.fyg($$0, $$1, $$2)

    def computeNext(self, ):
        return self.obj.computeNext()
