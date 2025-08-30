import jpype
import jpype.imports

# Auto-generated wrapper for a
class aWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = a(*args, **kwargs)

    def hasNext(self, ):
        return self.obj.hasNext()

    def next(self, ):
        return self.obj.next()

    def NoSuchElementException(self, ):
        return self.obj.NoSuchElementException()

    def remove(self, ):
        return self.obj.remove()

    def IllegalStateException(self, ):
        return self.obj.IllegalStateException()
