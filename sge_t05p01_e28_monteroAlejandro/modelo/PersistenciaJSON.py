import json

class Persistencia:
    #def escribirJSON():

    def leerJSON(nombreFichero):
        fp=open(nombreFichero,"r")
        fileData=json.load(fp)
        print(fileData)
        fp.close()
        return fileData
        