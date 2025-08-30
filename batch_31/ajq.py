import jpype
import jpype.imports

# Auto-generated wrapper for ajq
class ajqWrapper:
    def __init__(self, *args, **kwargs):
        self.obj = ajq(*args, **kwargs)

    def lastModifiedTime(self, ):
        return self.obj.lastModifiedTime()

    def lastAccessTime(self, ):
        return self.obj.lastAccessTime()

    def creationTime(self, ):
        return self.obj.creationTime()

    def isSymbolicLink(self, ):
        return self.obj.isSymbolicLink()

    def isOther(self, ):
        return self.obj.isOther()

    def size(self, ):
        return self.obj.size()

    def fileKey(self, ):
        return self.obj.fileKey()
