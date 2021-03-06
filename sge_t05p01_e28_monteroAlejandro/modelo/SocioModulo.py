from modelo.UsuarioModulo import Usuario
from modelo.BicicletaModulo import Bicicleta

class Socio: 
    def __init__(self, usuarioAsociado: Usuario, nombreCompleto, direccion, telefono, correoElectronico, bicicletas=[], familia={'Pareja':None,"Hijos":[],"Padres":[]}):
        self._usuarioAsociado=usuarioAsociado
        self._nombreCompleto=nombreCompleto
        self._direccion=direccion
        self._telefono=telefono
        self._correoElectronico=correoElectronico
        self._bicicletas=bicicletas
        self._familia=familia

    '''def __init__(self, nombreCompleto, direccion, telefono, correoVerElectronico):
        self._nombreCompleto=nombreCompleto
        self._direccion=direccion
        self._telefono=telefono
        self._correoElectronico=correoElectronico
        self.bicicletas=None
        self.familia=None

    def convertirSocioAJson(self):
        dictSocios = {"nombreCommpleto":self._nombreCompleto, "direccion":self._direccion, "telefono":self._telefono, "correoElectronico":self._correoElectronico}
        return dictSocios'''