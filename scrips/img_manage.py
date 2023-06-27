import os
import db_manage as _db

imgUnsaved = '../img/unsaved/'
imgSaved = '../img/saved/'

# Obtener la lista de archivos en el directorio
files = os.listdir(imgUnsaved)

# Imprimir los nombres de los archivos
for file in files:
    print(file)
    decition = input("Desea guardar la imagen:(y/n) ")
    if decition == "y":
        description = input("Que descripción le quiere poner: ")
        history = input("Desea que sea una historia:(y/n) ")
        if history == "y":
            history = 1
        else:
            history = 0
        hastags = input("Que hastags le quiere poner: ")
        url = imgSaved + file


        photos = _db.seephotos()

        flag = True

        for foto in photos:
            if foto[len(foto)-1] == url:
                flag = False
        
        if flag:
            _db.newphoto(description, history, hastags, url )
            os.system("mv " + imgUnsaved + file + " " + imgSaved + file)
            print("Ya se ha guradado y movido")
        else:
            print("la imagen ya existe, losiento")



