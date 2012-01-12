import re

class FunctionMap:
    def __init__(self):
        self._funcMap = None
    def registerFunctionMap(self, funcMap):
        self._funcMap = funcMap
    def callFunction(self, name):
        if self._funcMap:
            if self._funcMap.get(name):
                return self._funcMap[name]()
class Foo:
    def __init__(self):
        self._funcMap = dict()
        self.__initFunctionMap__()
    def __initFunctionMap__(self):
        self._funcMap["test1"] = self.test1
        self._funcMap["test2"] = self.test2
    def test1(self):
        print ("Test case 1")
    def test2(self):
        print ("Test Case 2")
    def getFunctionMap(self):
        return self._funcMap
def testFunctionMap():
    functionMap = FunctionMap()
    foo = Foo()
    functionMap.registerFunctionMap(foo.getFunctionMap())
    functionMap.callFunction("test1")
    functionMap.callFunction("test2")

class IBoo:
    TEST1=1
    TEST2=2
    def __init__(self):
        self._name = "IBoo"
    def test1(self):
        pass
    def test2(self,line):
        pass

class Boo(IBoo):
    def __init__(self):
        self._name = "Boo"
    def test1(self):
        print ("%s: Test1 called" % self._name)
    def test2(self,line):
        print ("%s: Test2 called with para %s" % (self._name, line))
        
class BooFactory:
    @staticmethod
    def createBooMapping(IBoo):
        test = dict()
        test[IBoo.TEST1] = (IBoo.test1, IBoo.test2)
        test[IBoo.TEST2] = (IBoo.test2, IBoo.test1)
        return test

def testBooFactory():
    bInstance = Boo()
    mapping = BooFactory.createBooMapping(bInstance)
    mapping[IBoo.TEST1][0]()
    mapping[IBoo.TEST1][1]("Test2")
    mapping[IBoo.TEST2][0]("Test2")

# ways to access base class methond/constructor    
class A(object):
    def __init__(self):
        print "Constructor A was called"

class B(A):
    def __init__(self):
        super(B,self).__init__()
        print "Constructor B was called"

class C(B):
    def __init__(self):
#        super(C,self).__init__()
        B.__init__(self)
        print "Constructor C was called"

class D:
    x = 1
    def test(self):
        print ("D:test called: %d" % self.x)
        
class E (D):
    x = 5
    def test(self):
        D.test(self)
        print ("E:test called: %d" % self.x)
    
class F:
    def __init__(self):
        self._test = 1
    def test(self):
        pass

class G (F):
    def test(self):
        print (self._test)
        
def testLongNameRegEx(value, testText):
    longNameRegExTemp = "(?P<prefix>^(>> |   ))(?P<name>[^ ]{%d,}) $"
    longNameRegEx = longNameRegExTemp % (value-1)
    print longNameRegEx
    result = re.search(longNameRegEx, testText)
    if result:
        print (result.group('prefix'))
        print (result.group('name'))
def testNameValueRegEx(value, testText):
    nameValueRegExTemp = "(?P<prefix>^(>> |   ))(?P<name>[^ ]{1,%d})[ ]{0,%d}(?P<value>[^ ]+$)"
    nameValueRegEx = nameValueRegExTemp % (value-1, value-2)
#    nameValueRegExTemp = "(?P<prefix>^(>> |   ))(?P<name>[^ ]{1,%d}) ?(?P<value>[^ ]+$)"
#    nameValueRegEx = nameValueRegExTemp % (value-1)
    print nameValueRegEx
    result = re.search(nameValueRegEx, testText)
    if result:
        print (result.group('prefix'))
        print (result.group('name'))
        print (result.group('value'))
    else:
        print ("No match for %s" % testText)
def testLongNameRegularExp(testText):
    longNameTemplate = re.compile(r"(?P<prefix>^(>> |   ))(?P<name>[^ \"]+(\"[^\"]+\")?[^ \"]?) $")
    result = longNameTemplate.search(testText)
    if result:
        print result.group('prefix')
        print result.group('name')
    else:
        print ("No Match for %s" % testText)
if __name__ == '__main__':
    testFunctionMap()
    testBooFactory()
    c = C()
    e = E()
    e.test()
    g = G()
    g.test()
    testLongNameRegEx(14, '''   KEYWORD("CONDITION" ''')
    testNameValueRegEx(21, '''   ^XTMP("PRCA219P"    PRCA219P*!''')
    testNameValueRegEx(21, '''   ^XTMP("MAGEVALSTUDY"RULES+36,RULES+90*''')
    testNameValueRegEx(14, '''   ADJUST       ADJNUM+1~,ADJNUM+3*,ADJNUM+4''')
    testNameValueRegEx(14, '''   ^RC("PRC ABJ"        RCCPCBAK+15''')
    testLongNameRegularExp('''   ZTSAVE("PRCAIO" ''')
    print ("Test"[0:2])

    

        
    