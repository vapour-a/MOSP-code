import jpype
import jpype.imports

# Auto-generated wrapper for gk
class gkWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = gk(*args, **kwargs)

    def acq(self, "ask_server"):
        return self.obj.acq("ask_server")

    def acq(self, "all_recipes"):
        return self.obj.acq("all_recipes")

    def acq(self, "available_sounds"):
        return self.obj.acq("available_sounds")

    def acq(self, "summonable_entities"):
        return self.obj.acq("summonable_entities")

    def a(self, $$0, $$1):
        return self.obj.a($$0, $$1)

    def IllegalArgumentException(self, $$0):
        return self.obj.IllegalArgumentException($$0)

    def a(self, $$0, $$1):
        return self.obj.a($$0, $$1)

    def a(self, $$0):
        return gk.a($$0)

    def a(self, $$0):
        return gk.a($$0)

    def b(self, $$0):
        return gk.b($$0)

    def a(self, $$0, $$1):
        return self.obj.a($$0, $$1)

    def getSuggestions(self, $$0, $$1):
        return self.obj.getSuggestions($$0, $$1)
