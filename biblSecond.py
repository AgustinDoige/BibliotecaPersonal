import pickle

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
    return tlis[0]+int(tlis[1])

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
        return

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

    def addBook(self,book):
        if (book.leg == 'AAA-000'):
            print("Legajo generico detectado.\nLlamando self.generateNewLeg()")
            book.leg = self.generateNewLeg()
        print("Imprimiendo libro para agregar:")       
        print(book)
        if getBool("¿Agregar este libro?"):
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
                ind = self.leglis.index(prevleg)
            except Exception:
                print("Legajo introducido no encontrado en biblioteca.\nRegenerando.")
                return self.generateNewLeg()
            if getBool("¿Mostrar legajos cercanos?"):
                print(self.leglis[ind-7:ind+8])
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
            nextLeg = self.getNextIndLeg(prevleg)
            if (prevleg[0]==nextLeg[0]):
                lAns = unparleg(prevleg[0],)
            else:
                pass
                #TODO TODO TODO TODO TODO TODO TODO TODO TODO
            
            
    def getNextIndLeg(self,l):
        #returns the next logged book in the library
        try:
            return self.leglis.index(l)+1
        except ValueError:
            tilt("Error in getNextIndLeg. input argument: {}".format(l))

    def markAsRemoved(self,leg):
        #use list.remove(element)
        # book = self.catalog[leg]
        pass
    
    def deleteBook(self,leg):
        pass

    def editBook(self,leg):
        pass

    def saveIntoFile(self,filename):
        #creates a file with filename and saves contents of the library in a parsable text form
        pass

    def loadLibraryFromFile(self,filename):
        #abre la forma parsable creada por saveIntoFile y carga todos los datos a la biblioteca
        pass

    def saveClassObject(self,filename):
        #use pickle
        pass