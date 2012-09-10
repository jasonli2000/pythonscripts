import json
from json import JSONEncoder


def testJson():
    outFile = open("C:/Temp/JSONTest/out.json",'wb')
#    package = {"1":1, "2":2}
#    json.dump(package,outFile)
#    package = Package("TestA")
#    json.dump(package, outFile, cls=PackageEncoder)
    data = [1,2,3,4,5]
    output =  JSONEncoder().encode(data)
    print output
if __name__ == '__main__':
    testJson()