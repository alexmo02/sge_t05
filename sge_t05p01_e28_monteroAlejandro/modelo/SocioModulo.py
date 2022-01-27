from modelo.UsuarioModulo import Usuario
from modelo.BicicletaModulo import Bicicleta

class Socio: 
    def __init__(self, usuarioAsociado: Usuario, nombreCompleto, direccion, telefono, correoElectronico):
        self._usuarioAsociado=usuarioAsociado
        self._nombreCompleto=nombreCompleto
        self._direccion=direccion
        self._telefono=telefono
        self._correoElectronico=correoElectronico
        self.bicicletas=None
        self.familia=None
