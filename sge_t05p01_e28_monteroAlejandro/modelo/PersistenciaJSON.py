import json

class Persistencia:
    #def escribirJSON():

    def leerJSON(nombreFichero):
        fp=open(nombreFichero,"r")
        fileData=json.load(fp)
        print(fileData)
        fp.close()
        return fileData

    def writeJSON(d:dict,filename):
        with open(filename, "r+") as file:
            data = json.load(file)
            data.append(d)
            file.seek(0)
            json.dump(data, file,indent=4)
        