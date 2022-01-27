from re import S
from modelo.Prueba import Prueba
from vista.VistaAdmin import VistaAd
from modelo.ClubModulo import Club
from modelo.SocioModulo import Socio

class ControladorAd:
    def __init__(self, club : Club, usuario, contrasenna):
        self._club=club
        self._vistaAd=VistaAd(self)
        self.inicio(usuario, contrasenna)
    
    def inicio(self, usuario, contrasenna):
        Prueba.cargarUsuarios(self._club)
        Prueba.cargarSocios(self._club)
        respuesta = self._club.verificarUsuarioAd(usuario, contrasenna)
        if(respuesta == 1):
            self._vistaAd.mostrarMenu(usuario)
        elif(respuesta == 2): 
            self._vistaAd.mostrarError("El usuario y la contraseña no existen")
        else:
            self._vistaAd.mostrarError("No tienes los permisos para acceder")

    def listarSocios(self):
        lista = []
        for clave in self._club._diccSocios:
            valor = self._club._diccSocios[clave]
            lista.append(valor._nombreCompleto)
        self._vistaAd.muestraSocios(lista)

    def controlOpciones(self,opc):
        if (opc == 0):
            self._vistaAd.salir()
        elif (opc == 1):
            self.listarSocios()
