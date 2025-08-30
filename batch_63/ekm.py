import jpype
import jpype.imports

# Auto-generated wrapper for ekm
class ekmWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = ekm(*args, **kwargs)

    def ekm(self, $$0, $$1, $$2):
        return self.obj.ekm($$0, $$1, $$2)

    def ekm(self, $$0, $$1):
        return self.obj.ekm($$0, $$1)

    def getMessage(self, ):
        return self.obj.getMessage()

    def error(self, %d/%d):
        return self.obj.error(%d/%d)

    def error(self, %d):
        return self.obj.error(%d)

    def a(self, $$0):
        return self.obj.a($$0)
