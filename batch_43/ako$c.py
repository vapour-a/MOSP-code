import jpype
import jpype.imports

# Auto-generated wrapper for c
class cWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = c(*args, **kwargs)

    def c(self, $$0, $$1, $$2):
        return self.obj.c($$0, $$1, $$2)

    def Exception(self, "Stacktrace"):
        return self.obj.Exception("Stacktrace")

    def StringWriter(self, ):
        return self.obj.StringWriter()

    def PrintWriter(self, $$3):
        return self.obj.PrintWriter($$3)

    def close(self, ):
        return self.obj.close()

    def finalize(self, ):
        return self.obj.finalize()
