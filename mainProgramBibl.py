import biblSecond as b
import pickle

def main2():
    libroa = b.Libro()
    libroa.leg = "ABC-050"
    #print(libroa)
    bookDic = {"leg":"BBB-500",
            "title":"Juego de Tronos: Cancion de Hielo y Fuego I",
            "author":"George R.R. Martin",
            "genre":"fantasy",
            "stateLib":"disponible",
            "location":"fisica",
            "stateLec":"leido",
            "owner":"propio"}
    librob = b.Libro(bookDic)
    bookDic = {"leg":"XXZ-500",
            "title":"Harry Potter y la Orden del Fenix",
            "author":"J.K. Rowling",
            "genre":"fantasy",
            "stateLib":"disponible",
            "location":"fisica",
            "stateLec":"leido",
            "owner":"propio"}
    libroc = b.Libro(bookDic)
    bibl = b.Biblioteca()
    bibl.addBook(libroa)
    bibl.addBook(librob)
    bibl.addBook(libroc)
    bibl.saveClassObject("classObj.cls")

def main():
    with open("classObj.cls","rb") as file:
        bibl = pickle.load(file)
    print(bibl)

    

#self.leg = arg["leg"]
#self.title = arg["title"]
#self.author = arg["author"]
#self.genre = arg["genre"]
#self.stateLib = arg["stateLib"]
#self.stateLec = arg["stateLec"]
#self.location = arg["location"]
#self.owner = arg["owner"]


main()