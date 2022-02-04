from ast import arg
import sys

from vista.VistaAdmin import VistaAd
from vista.VistaUsuario import VistaUs
from modelo.ClubModulo import Club
from modelo.Prueba import Prueba
from controlador.ControladorAdmin import ControladorAd
from controlador.ControladorUsuario import ControladorUs

if __name__ == "__main__":

    #Definimos un Club
    club = Club("Los Satanases del Infinero", "11111111D")
    Prueba.cargarUsuarios(club)
    #controlador_ad = ControladorAd(club)
    #argumentos=["app.py","-u", "11111111A", "-p", "admin", "-A"]
    #argumentos=["app.py","-u", "22222222B", "-p", "usuario1"]
    argumentos = sys.argv
    if (club.verificarUsuarioAdmin(argumentos)):
        controlador = ControladorAd(club, argumentos[2], argumentos[4])
    else:
        controlador = ControladorUs(club, argumentos[2], argumentos[4])

    


       