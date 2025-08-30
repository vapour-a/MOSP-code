import jpype
import jpype.imports

# Auto-generated wrapper for c
class cWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = c(*args, **kwargs)

    def c(self, $$0, $$1):
        return self.obj.c($$0, $$1)

    def hasNext(self, ):
        return self.obj.hasNext()

    def nextInt(self, ):
        return self.obj.nextInt()

    def NoSuchElementException(self, ):
        return self.obj.NoSuchElementException()

    def a(self, $$0, $$1):
        return c.a($$0, $$1)

    def c(self, $$0, $$1):
        return self.obj.c($$0, $$1)
