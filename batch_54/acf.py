import jpype
import jpype.imports

# Auto-generated wrapper for acf
class acfWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = acf(*args, **kwargs)

    def a(self, $$0, $$1, $$2, $$3, $$4, $$5):
        return self.obj.a($$0, $$1, $$2, $$3, $$4, $$5)

    def if(self, $$13):
        return self.obj.if($$13)

    def a(self, paramIterator, paramInt1, paramInt2, paramInt3, paramInt4):
        return self.obj.a(paramIterator, paramInt1, paramInt2, paramInt3, paramInt4)
