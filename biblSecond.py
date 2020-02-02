#encoding utf-8
import pickle
import json

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

def tilt(msg):
    print(msg+"\n\tTilt.")
    while True:
        pass

def getBool(inputMessage):
    assert(type(inputMessage)==type("string"))
    im = inputMessage+"\t(y/n)   "
    while True:
        inp = input(im).lower()
        if (inp == 'y'):
            return True
        elif (inp == 'n'):
            return False

def getString(inputMessage):
    while True:
        caden = input(inputMessage+"\t")
        if getBool("Input Leido:\n\t'{}'\n¿Confirmar?".format(caden)):
            return caden

def parleg(leg):
    tlis = leg.split("-")
    return [tlis[0],int(tlis[1])]

def unparleg(leglist):
    return leglist[0]+'-'+str(leglist[1]).zfill(3)

def isValidLeg(leg):
    tlis = leg.split("-")
    if ((len(tlis)!=2) or (len(tlis[0])!=3) or (len(tlis[1])!=3)):
        return False
    try:
        _ = int(tlis[1])
    except Exception:
        return False
    return True

def logDict(dic,key,item):
    """Tries to log item in the list of the dictionary in order. If such key with list doens't exist. It creates it."""
    try:
        AddInOrder(dic[key],item)
    except KeyError:
        dic[key] = [item]

def nextLetterTrio(st):
    #  returns AAB from AAA, ABA from AAZ and so on
    alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    if st[2]=="Z":
        if st[1]=="Z":
            if st[0]=="Z":
                tilt("ERROR: Input 'ZZZ' to nextLetterTrio function.")
            return alphabet[alphabet.index(st[0])+1]+"AA"
        return st[0]+alphabet[alphabet.index(st[1])+1]+"A"
    return st[0]+st[1]+alphabet[alphabet.index(st[2])+1]

def averageLetterTrio(st1,st2):
    alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    if st1[0]==st2[0]:
        if st1[1]==st2[1]:
            in1 = alphabet.index(st1[2])
            in2 = alphabet.index(st2[2])
            return st1[:-1]+alphabet[round((in1+in2)/2)] #RISK: AAA and AAB would get AAA
        in1 = alphabet.index(st1[2])
        in2 = alphabet.index(st2[2])






class Libro:
    def __init__(self,arg=''):
        # Legajo Nombre Autor Genero Estado_de_Libro Estado_de_Lectura
        # LEG:  AAA-000
        #No arg: LIBRO GENERICO
        # arg=1 Encuesta por consola
        # arg=2 diccionario con libro
        if (arg==1):
            self.crearLibro()
            return
        elif (type(arg)==type(dict())):
            try:
                pass
                self.leg = arg["leg"]
                self.title = arg["title"]
                self.author = arg["author"]
                self.genre = arg["genre"]
                self.stateLib = arg["stateLib"]
                self.stateLec = arg["stateLec"]
                self.location = arg["location"]
                self.owner = arg["owner"]
                return
            except Exception:
                print("Error: Diccionario con formato desconocido.")

        elif (arg!=''):
            print("Error: Argumento de iniciacion de Libro no esperado.")
        print("Generando Libro Generico.")
        self.leg = "AAA-000"
        self.title = "LIBRO DESCONOCIDO"
        self.author = "AUTOR DESCONOCIDO"
        self.genre = "GENERO DESCONOCIDO"
        self.stateLib = "disponible"
        self.stateLec = "no leido"
        self.location = "fisica"
        self.owner = "propio"

    def crearLibro(self):
        self.title = getString("Titulo del libro:")
        self.author = getString("Autor del libro:")
        self.genre = getString("Genero del libro:")
        
        if (getBool("¿Esta disponible?")):
            self.stateLib = "disponible"
        elif(getBool("¿Fue prestado?")):
            self.stateLib = "prestado"
        else:
            self.stateLec = "no disponible"

        if(getBool("¿Es para la biblioteca fisica?")):
            self.location = "fisica"
        else:
            self.location = "digital"

        if(getBool("¿El libro es propio?")):
            self.owner = "propio"
        else:
            self.owner = getString("Owner:")
        
        if(getBool("¿Fue ya leido?")):
            self.stateLec = "leido"
        elif(getBool("¿No leido?")):
            self.stateLec = "no leido"
        elif(getBool("¿Abandonado?")):
            self.stateLec = "abandonado"
        else:
            self.stateLec = "en progreso"

        if(getBool("¿El libro esta disponible?")):
            self.stateLib = "disponible"
        elif(getBool("¿Fue prestado?")):
            self.stateLib = "prestado"
        else:
            self.stateLib = "no disponible"
        
    def confirmData(self):
        #Goes through every data saved in Book and asks for console confirmation. It modifies the data that is wrong.
        print("Confirming Book Information")
        print(self)
        if getBool("Is everything correct?"):
            return
        if getBool(f"is (leg='{self.leg}') incorrect?"):
            self.leg = getString("Input leg")
        if getBool(f"is (title='{self.title}') incorrect?"):
            self.title = getString("Input title")
        if getBool(f"is (author='{self.author}') incorrect?"):
            self.author = getString("Input author")
        if getBool(f"is (stateLib='{self.stateLib}') incorrect?"):
            self.stateLib = getString("Input stateLib")
        if getBool(f"is (stateLec='{self.stateLec}') incorrect?"):
            self.stateLec = getString("Input stateLec")
        if getBool(f"is (location='{self.location}') incorrect?"):
            self.location = getString("Input location")
        if getBool(f"is (owner='{self.owner}') incorrect?"):
            self.owner = getString("Input owner")       
    
    def shStr(self):
        #Returns a one line short informtion about a book
        return f"({self.leg}-{self.title})"
    
    def getBookDict(self):
        #RETURNS A DICTIONARY WITH THE RELEVANT INFORMATION. A DICT THAT COULD BE USED AS A ARGUMENT TO CREATE A NEW DICT
        pass

    def __str__(self):
        anStr = f"Libro {self.leg}::\n\t{self.title} - {self.author}\tGenero: {self.genre}\n\tEstado: {self.stateLib} y {self.stateLec}.\t"
        if (self.location!="fisica"):
            anStr = anStr + "Archivado Digitalmente"
        elif (self.owner=="propio"):
            anStr = anStr + "Libro Propio."
        else:
            anStr = anStr + f"Owner: {self.owner}"
        return anStr
            
class Biblioteca:
    def __init__(self):
        self.leglis = [] #Lista EN ORDEN de libros cargados a la biblioteca
        self.catalog = {} #Diccionario de objetos de la clase "Libro" con key=leg
        self.authorDic = {} #Diccionario de leg con key=authorStr
        self.genreDic = {} #Diccionario de leg con key=genreStr
        self.stateLibDic = {'disponible':[],'prestado':[],'no disponible':[]} #Diccionario de leg con key=libStateStr
        self.stateLecDic = {'leido':[],'no leido':[],'abandonado':[],'en progreso':[]} #Diccionario de leg con key=lecStateStr
        self.ownerDic = {'propio':[]}
        self.locationDic = {'fisica':[],'digital':[]}

    def addBook(self,book,getConfirm=True):
        if (book.leg == 'AAA-000'):
            print("Legajo generico detectado.\nLlamando self.generateNewLeg()")
            book.leg = self.generateNewLeg()
        print("Imprimiendo libro para agregar:")       
        print(book)
        if (getConfirm==False) or (getBool("¿Agregar este libro?")):
            try:
                _ = self.catalog[book.leg]
                tilt("ERROR: Tried to add book with a leg already used by the following book:\n{}".format(self.catalog[book.leg]))
            except Exception:
                pass
            self.catalog[book.leg] = book
            AddInOrder(self.leglis,book.leg)

            bklg = book.leg
            logDict(self.authorDic  ,book.author  ,bklg)
            logDict(self.genreDic   ,book.genre   ,bklg)
            logDict(self.stateLibDic,book.stateLib,bklg)
            logDict(self.stateLecDic,book.stateLec,bklg)
            logDict(self.ownerDic   ,book.owner   ,bklg)
            logDict(self.locationDic,book.location,bklg)
            del bklg
        elif not getBool("¿Fix Book?"):
            print("Log Cancelado.")
            return
        book.confirmData()
        

    def avaliableLeg(self,leg):
        #devuelve True si el legajo introducido no esta usado en la biblioteca
        try:
            _ = self.catalog[leg]
            return False
        except KeyError:
            return True

    def generateNewLeg(self):
        if (getBool("¿Ya se tiene legajo elegido?")):
            legGen = getString("Introducir legajo:")
            if (self.avaliableLeg(legGen)):
                if isValidLeg(legGen):
                    return legGen
                else:
                    print("Error: legajo Invalido.\nRegenerando.")
                    return self.generateNewLeg()
            else:
                print("Error: legajo Ocupado\nRegenerando.")
                return self.generateNewLeg()
        else:
            print("Generando legajo.")
            sucesorInmediatoBool = getBool("Legajo sucesor:\n\tEl numero obtenido es el inmediatamente siguiente al libro anterior, sin posibilidad de futuros libros en el medio. Reservado para secuelas o volumenes.\n¿Es un legajo sucesor?")
            prevleg = parleg(getString("Introducir legajo anterior:"))
            try:  #Seeing if leg introduced exists
                ind = self.leglis.index(unparleg(prevleg))
                if getBool("Imprimir Legajos Cercanos?"):
                    if (ind-7>0):
                        print(self.leglis[ind-7:ind+7])
                    else:
                        print(self.leglis[0:ind+7])
            except Exception:
                print("Legajo introducido no encontrado en biblioteca.\nRegenerando.")
                return self.generateNewLeg()
            if(sucesorInmediatoBool):
                if (prevleg[1]==999):
                    lAns = unparleg([nextLetterTrio(prevleg[0]),0])
                else:
                    lAns = unparleg([prevleg[0],prevleg[1]+1])
                if not self.avaliableLeg(lAns):
                    print("Error: Legajo sucesor inmediato no disponible.\nRegenerando.")
                    return self.generateNewLeg()
                print("Legajo generado: {}")
                if not getBool("¿Confirmar?"):
                    print("Regenerando.")
                    return self.generateNewLeg()
                else:
                    return lAns
            # IMPLICIT ELSE: sucesorInmediatoBool = False
            nextLeg = parleg(self.getNextIndLeg(prevleg))
            if (prevleg[0]==nextLeg[0]):
                return unparleg([prevleg[0],round((prevleg[1]+nextLeg[1])/2)])
            # IMPLICIT ELSE: Need aerage between two 3-LETTERS words
            # TODO FIX getAverageLeg doesn't know what to do when AAA and AAB
            ####lAns = getAverageLeg(unparleg(prevleg))
            if not self.avaliableLeg(lAns):
                print(f"Error: Legajo Generado ({lAns}) no disponible.\nRegenerando.")
                return self.generateNewLeg()
            return lAns

    def getNextIndLeg(self,l):
        #returns the next logged book in the library
        try:
            return self.leglis.index(l)+1
        except ValueError:
            tilt("Error in getNextIndLeg. input argument: {}".format(l))
    
    def deleteBook(self,leg):
        try:
            book = self.catalog[leg]
        except KeyError:
            print(f"Trying to delete {leg}. Book not found on Bibl Catalog")
            print("Deletion Missed")
        del self.catalog[leg]
        self.leglis.remove(leg)
        self.authorDic[book.author].remove(leg)
        self.genreDic[book.genre].remove(leg)
        self.stateLecDic[book.stateLec].remove(leg)
        self.stateLibDic[book.stateLib].remove(leg)
        self.ownerDic[book.owner].remove(leg)
        self.locationDic[book.location].remove(leg)

    def editBook(self,leg):
        try:
            print("Change leg to 'AAA-000' to generate new leg")
            book = self.catalog[leg]
        except KeyError:
            print(f"Trying to edit {leg}. Book not found on Bibl Catalog")
            print("Missing Edition")
        self.deleteBook(book)
        book.confirmData()
        self.addBook(book)

    def saveIntoFile(self,filename):
        bookLis = []
        for lg in self.leglis:
            book = self.catalog[lg]
            bookLis.append(book.getBookDict())
        with open(filename,"w") as g:
	        json.dump(bookLis,g,indent=2)

        # TODO TEST TODO TEST TODO TEST TODO TEST TODO TEST TODO TEST
        # AFTER FINISHING getBookDict test if this works. I don't know if you can save lists as json

    def loadLibraryFromFile(self,filename):
        with open(filename,"r") as g:
	        bookLis = json.load(g)
        for bk in bookLis:
            self.addBook(bk,getConfirm=False)
            print(f"Added {bk.shStr()}.")

    def saveClassObject(self,filename):
        with open(filename,'wb') as file:
            pickle.dump(self,file)

    def __str__(self):
        line = "______________________________________________"
        strLis = ["\n",line,"\n"]
        for l in self.leglis:
            strLis.append(self.catalog[l].shStr())
            strLis.append("\n")
        strLis.append(f"\n{line}\nBy Author:\n")
        for aut in self.authorDic:
            strLis.append(f"\n\t{aut}:")
            for bk in self.authorDic[aut]:
                strLis.append(self.catalog[bk].shStr())
                strLis.append("\t")
        strLis.append(f"\n{line}\nBy Genre:\n")
        for gen in self.genreDic:
            strLis.append(f"\n\t{gen}:")
            for bk in self.genreDic[gen]:
                strLis.append(self.catalog[bk].shStr())
                strLis.append("\t")
        ans = ''
        for st in strLis:
            ans += st
        return ans