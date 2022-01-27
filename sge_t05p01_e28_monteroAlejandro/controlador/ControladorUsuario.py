from modelo.Prueba import Prueba
from vista.VistaUsuario import VistaUs
from modelo.ClubModulo import Club

class ControladorUs:
    def __init__(self, club : Club, usuario, contrasenna):
        self._club=club
        self._vistaUs=VistaUs(self)
        self.inicio(usuario, contrasenna)
    
    def inicio(self, usuario, contrasenna):
        Prueba.cargarUsuarios(self._club)
        Prueba.cargarSocios(self._club)
        if(self._club.verificarUsuarioUs(usuario, contrasenna)):
            self._vistaUs.mostrarMenu()
        else:
            self._vistaUs.mostrarError("El usuario y la contraseña no existen")

