import jpype
import jpype.imports

# Auto-generated wrapper for null
class nullWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = null(*args, **kwargs)

    def tryAdvance(self, $$0):
        return self.obj.tryAdvance($$0)

    def trySplit(self, ):
        return self.obj.trySplit()

    def estimateSize(self, ):
        return self.obj.estimateSize()

    def characteristics(self, ):
        return self.obj.characteristics()
