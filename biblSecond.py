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

def getBool(inputMessage):
    assert(type(inputMessage)==type("string"))
    im = inputMessage+"\t(y/n)   "
    while True:
        inp = input(im).lower()
        if (inp == 'y'):
            return True
        elif (inp = 'n'):
            return False

def getString(inputMessage):
    while True:
        caden = input(inputMessage+"\t")
        if getBool("Input Leido:\n\t'{}'\n¿Confirmar?".format(caden)):
            return caden

def confirmStr(st):
    print("Cadena aceptada: \n\t'{}'")
    return getBool("¿Confirmar?")

def parleg(leg):
    return leg.split("-")

def unparleg(leglist):
    ans = ''
    for el in leglist:
        ans = ans+'-'+el
    return ans[1:]

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

    def addBook(self,bookObj):
        if (bookObj.leg == 'AAA-000'):
            print("Legajo generico detectado")
            bookleg = self.generateNewLeg()

    def avaliableLeg(leg):
        #devuelve True si el legajo introducido no esta usado en la biblioteca
        return True          

    def generateNewLeg(self):
        if (getBool("¿Ya se tiene legajo elegido?")):
            legGen = getString("Introducir legajo:")
        else:
            print("Generando legajo.")
            if getBool("Legajo sucesor:\n\tEl numero obtenido es el inmediatamente siguiente al libro anterior, sin posibilidad de futuros libros en el medio. Reservado para secuelas o volumenes.\n¿Es un legajo sucesor?"):
                prevleg = parleg(getString("Introducir legajo anterior:"))
                tempList = prevleg[:-1]
                tempList.append(int(prevleg[-1])+1)
                lAns = unparleg(tempList)
                print("Legajo generado: {}")
                if not getBool("¿Confirmar?"):
                    print("Regenerando...")
                    return self.generateNewLeg()
                else:
                    return lAns
            #TODO:: AGREGAR EL PROMEDIO DE DOS PARSED LEGS.
            return "AAA-000"

    def getNextLeg(self,l):
        #goes through the list and finds the book that follows l
        lAns = "AAA-000"
        return lAns
        

    def markAsRemoved(self,leg):
        #user list.remove(element)
        book = self.catalog[leg]

    
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