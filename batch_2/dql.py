import jpype
import jpype.imports

# Auto-generated wrapper for dql
class dqlWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = dql(*args, **kwargs)

    def dql(self, $$0, $$1, $$2):
        return self.obj.dql($$0, $$1, $$2)

    def a(self, $$0, $$1, $$2):
        return dql.a($$0, $$1, $$2)

    def dql(self, $$0, $$1, $$2):
        return self.obj.dql($$0, $$1, $$2)

    def a(self, $$0, $$1):
        return self.obj.a($$0, $$1)

    def a(self, ):
        return self.obj.a()

    def toString(self, ):
        return self.obj.toString()
