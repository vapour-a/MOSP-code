import jpype
import jpype.imports

# Auto-generated wrapper for dgb
class dgbWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = dgb(*args, **kwargs)

    def a(self, paramInt):
        return self.obj.a(paramInt)

    def a(self, paramUUID):
        return self.obj.a(paramUUID)

    def a(self, ):
        return self.obj.a()

    def a(self, dfz<T, paramdfz, paramanr):
        return self.obj.a(dfz<T, paramdfz, paramanr)

    def a(self, parameed, paramConsumer):
        return self.obj.a(parameed, paramConsumer)

    def a(self, dfz<T, paramdfz, parameed, paramanr):
        return self.obj.a(dfz<T, paramdfz, parameed, paramanr)
