#encoding utf-8
import biblSecond as b

def RunTest(test):
    try:
        a = test()
    except Exception:
        print("Meta Error in Test: {}".format(test.__name__))
        test()
    if a != 1:
        for e in a:
            print(f"{test.__name__}: ",e)
        return 0
    return 1

def testAddInOrder():
    griefs = []
    testList = [1,3]
    b.AddInOrder(testList,2)
    if testList != [1,2,3]:
        griefs = ["Failed [1,3]<-2"]
    testList = ["1","3"]
    b.AddInOrder(testList,"2")
    if testList != ["1","2","3"]:
        griefs.append("Failed ['1','3']<-'2'")
    testList = [1,2,3,4]
    b.AddInOrder(testList,5)
    if testList != [1,2,3,4,5]:
        griefs.append("Failed [1,2,3,4]<-5")
    testList = [2,3,4]
    b.AddInOrder(testList,1)
    if testList != [1,2,3,4]:
        griefs.append("Failed [2,3,4]<-1")
    testList = [2,3,4]
    b.AddInOrder(testList,3)
    if testList != [2,3,3,4]:
        griefs.append("Failed [2,3,4]<-3")
    if len(griefs)==0:
        return 1
    return griefs

def testgetBool():
    return 1
    if b.getBool("Enter y"):
        if not b.getBool("Enter n"):
            return 1
    return 0

def testgetString():
    return 1
    a = b.getString("Write String:")
    if type(a) == type("string"):
        return 1
    return ["Type of element is not string"]

def testparleg():
    griefs = []
    if b.parleg("ABZ-043") != ["ABZ",43]:
        griefs.append(f"Basic parsec of 'ABZ-043' returns {b.parleg('ABZ-043')}.")
    if b.unparleg(b.parleg('ABZ-043')) != 'ABZ-043':
        griefs.append(f"unparleg() is not the inverse of parleg():\tb.unparleg(b.parleg('ABZ-043')) = {b.unparleg(b.parleg('ABZ-043'))}")
    if len(griefs)==0:
        return 1
    return griefs

def testunparleg():
    griefs = []
    if b.unparleg(["ABZ",43]) != "ABZ-043":
        griefs.append(f"Basic upparsec of ['ABZ',43]' returns {b.unparleg(['ABZ',43])}.")
    if b.parleg(b.unparleg(["ABZ",43])) != ["ABZ",43]:
        griefs.append(f"unparleg() is not the inverse of parleg():\tb.parleg(b.unparleg(['ABZ',43])) = {b.parleg(b.unparleg(['ABZ',43]))}")
    if len(griefs)==0:
        return 1
    return griefs

def main():
    testList = [testAddInOrder,testgetBool,testgetString,testparleg,testunparleg]
    print("Running Tests.")
    passedTests = 0
    for t in testList:
        passedTests += RunTest(t)
    print("Tests Completed.")
    print("{}/{} tests passed.".format(passedTests,len(testList)))

main()


"""
FUNCTIONS TO ADD:
isValidLeg(leg)
logDict(dic,key,item)
nextLetterTrio(st)

class Libro
    def crearLibro(self)
    def confirmData(self)
    def __str__(self)
            
class Biblioteca:
    def __init__(self)
    def addBook(self,book)
    def avaliableLeg(self,leg)
    def generateNewLeg(self)
    def getNextIndLeg(self,l)
    def markAsRemoved(self,leg)
    def deleteBook(self,leg)
    def editBook(self,leg)
    def saveIntoFile(self,filename)
    def loadLibraryFromFile(self,filename)
    def saveClassObject(self,filename)"""