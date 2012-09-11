import json
from json import JSONEncoder

class Routine(object):
    def __init__(self, name):
        self._name = name
    def __repr__(self):
        return self._name
    
class Global(object):
    def __init__(self, name):
        self._name = name
    def __repr__(self):
        return self._name
    
class Package(object):
    def __init__(self, name):
        self._name = name
        self._globals = []
        self._routines = []
    def addRoutine(self, routine):
        self._routines.append(routine)
    
    def addGlobal(self, Global):
        self._globals.append(Global)

class TestJSONEncoder(JSONEncoder):
    def default(self, object):
        if isinstance(object, Package):
            return self.visitPackage(object)
        elif isinstance(object, Routine) or isinstance(object, Global):
            return object.__repr__()
        return super(TestJSONEncoder, self).default(object)
    def visitPackage(self, Package):
        packageNamePair = "\"Name\":\"%s\"" % Package._name
        AllRoutines = super(TestJSONEncoder, self).encode(Package._routines)
        RoutinesPair = "\"Routines\":%s" % AllRoutines
        AllGlobals = super(TestJSONEncoder,self).encode(Package._globals)
        GlobalsPair = "\"Globals\":%s" % AllGlobals
        return "{%s,%s,%s}" % (packageNamePair, RoutinesPair, GlobalsPair)

testFileName = "C:/Temp/JSONTest/out.json"            
def testJson():
    outFile = open(testFileName,'wb')
    data = [1,2,3,4,5]
    output =  JSONEncoder().encode(data)
    print output
    g1 = Global("GTest1")
    output = TestJSONEncoder().encode(g1)
    print output
    g2 = Global("GTest2")
    r1 = Routine("RTest1")
    r2 = Routine("RTest2")
    output = TestJSONEncoder().encode(r1)
    print output
    p1 = Package("PTest1")
    p1.addGlobal(g1)
    p1.addGlobal(g2)
    p1.addRoutine(r1)
    p1.addRoutine(r2)
#    json.dump(p1, outFile, cls=TestJSONEncoder)
    output = TestJSONEncoder().visitPackage(p1)
    outFile.write(output)
    outFile.write("\n")
    print output
    outFile.close()
    inputFile = open(testFileName, "rb")
    p1 = json.load(inputFile)
    print p1.keys()
if __name__ == '__main__':
    testJson()