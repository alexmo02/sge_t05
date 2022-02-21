
import sys
import json

from modelo.ClubModulo import Club
from modelo.Prueba import Prueba
from controlador.ControladorAdmin import ControladorAd
from controlador.ControladorUsuario import ControladorUs

if __name__ == "__main__":

    #Definimos un Club
    #club = Club("Los Satanases del Infinero", "11111111D")
    #Prueba.cargarUsuarios(club)

    with open("club.json", 'r') as f:
        info = json.load(f)
    for i in info:
        club = Club(i["_nombreClub"], i["_cif"], i["_sedeSocial"], i["_saldoTotal"], i["_controlCuotas"])

    #controlador_ad = ControladorAd(club)
    #argumentos=["app.py","-u", "11111111A", "-p", "admin", "-A"]
    #argumentos=["app.py","-u", "22222222B", "-p", "usuario1"]
    argumentos = sys.argv

    if(argumentos[1]=="-u" and argumentos[3]=="-p"):
        if (club.verificarUsuarioAdmin(argumentos)):
            controlador = ControladorAd(club, argumentos[2], argumentos[4])
        elif (club.verificarUsuarioUsuar(argumentos)):
            controlador = ControladorUs(club, argumentos[2], argumentos[4])
    else: 
        print("Debes introducir los parámetros -u y -p")
    


       