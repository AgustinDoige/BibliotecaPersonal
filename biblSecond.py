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

def confirmStr(st):
    print("Cadena aceptada: \n\t'{}'")
    return getBool("¿Confirmar?")

def promedioLeg(l1,l2):
    #devuelve el promedio de l1 y l2 consideando que l1 y l2 tienen la forma "AAA-000-..."
    lAns = "AAA-000"
    return lAns

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
        self.stateLib = "Disponible"
        self.stateLec = "No Leido"
        self.location = "Biblioteca Fisica"
        self.owner = "Propio"

    def crearLibro(self):
        while True:
            caden = input("Titulo del libro: ")
            if confirm(caden):
                self.title = caden
                break

        while True:
            caden = input("Autor del libro: ")
            if confirm(caden):
                self.author = caden
                break
        while True:
            caden = input("Genero del libro: ")
            if confirm(caden):
                self.genre = caden
                break
        
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
    
    def saveIntoFile(self,filename):
        #creates a file with filename and saves contents of the library in a parsable text form
        pass

    def loadLibraryFromFile(self,filename):
        #abre la forma parsable creada por saveIntoFile y carga todos los datos a la biblioteca
        pass