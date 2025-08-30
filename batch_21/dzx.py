import jpype
import jpype.imports

# Auto-generated wrapper for dzx
class dzxWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = dzx(*args, **kwargs)

    def and(self, $$0):
        return self.obj.and($$0)

    def or(self, $$0):
        return self.obj.or($$0)

    def expand(self, paramdzk, paramConsumer):
        return self.obj.expand(paramdzk, paramConsumer)
