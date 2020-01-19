"""
EJEMPLO DE DATABASE:
Legajo Nombre Autor Genero Estado_de_Libro Estado_de_Lectura
"""

import pickle

class Bookcase:
    def __init__(self):
        biblPersonal = Biblioteca(0)
        biblPrestados = Biblioteca(1)
        biblElectronica = Biblioteca(2)

class Biblioteca:
    def __init__(self,typ):
        self.type = typ
        self.database = {} # {leg:{INFORMATION}}
        self.legList = []
        self.titles = [] #(leg,title)
        self.authors = {}
        self.sections = {}
        self.rState = {"leido":[],"no leido":[],"en progreso":[]}
        if (typ==0):
            self.bState = {"disponible":[],"prestado":[],"perdido":[]}
        elif (typ==1):
            self.owners = {}
        else:
            self.locations = {}
    
    def addBook0(self,leg,bookName,autor,genero,bbstate='disponible',rrstate='no leido'):
        AddInOrder(self.legList,leg)
        AddInOrder(self.bState[bbstate],leg)
        AddInOrder(self.rState[rrstate],leg)
        AddInOrder(self.titles,(leg,bookName))
        try:
            AddInOrder(self.authors[autor],leg)
        except KeyError:
            self.authors[autor] = [leg]
    
    def updateBook0(self,leg,updateType,update):
        pass
    
    def markAsLost(self,leg):
        pass

    def purgeBook0(self,leg):
        #TODO Access information about entry and pinpoint places where it should be eliminated
        pass

    def writeReadableDatabase(self,filename):
        pass

    def searchAuthor(self,author):
        pass

    def searchTitle(self,title):
        pass

    def searchGenre(self,genre):
        pass

    def searchrState(self,rrState):
        pass

    def searchbState(self,bbState):
        pass

    def newBook(pass):
        pass

def AddInOrder(lis,it):
    "It adds an element in an ordered list in the correct place to preserve said order"
    i = 0
    while(True):
        try:
            if (it < lis[i]):
                lis.insert(i,it)
                break
            i += 1
        except IndexError:
            lis.append(it)
            break

def readRawDatabase(filename):
    rawDatabase = []
    with open(filename,'r') as f:
        while True:
            line = f.readline()
            if (line==''):
                break
            rawDatabase.append(line)
    return rawDatabase

def loadDatabaseClass():

def main():
    with open("database",'rb') as f:
        pickle.load(f)
        aObject = Object()
        pickle.dump(aObject,f)


main()
exit()
quit()
#TODO:
SOFT DELETE (Marks book as "Eliminado")
HARD DELETE (Fully deletes entry)
WRITE PARSE LINE FUNCTION
USE PICKLE TO SAVE ACTUAL DATABASE INSTEAD OF PARSING EVERYTIME
HAVE A BACKUP WHERE EVERYTHING IS ADDED TO A TEXT FILE DATABASE BUT WITHOUT 
    ORDER AND THAT IT IS NOT ACTUALLY USED BY THE PROGRAM
IMPLEMENT A SEARCH FUNCTION