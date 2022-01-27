from modelo.SocioModulo import Socio
from modelo.UsuarioModulo import Usuario
from modelo.ClubModulo import Club

class Prueba: 
    def cargarSocios(club : Club):
        #self._listaSocios = {'11111111A' : Usuario ("admin", "C/admin", 666777888, "admin@gmail.com")}
        #def __init__(self, usuarioAsociado: Usuario, nombreCompleto, direccion, telefono, correoElectronico, bicicletas: Bicicleta, familia):
        club.asignarListaSocios({'11111111A' : Socio (club.getUsuario('11111111A'), 'Alejandro Montero', 'c/direccion1', 666777888, "alejandro@gmail.com"),
        '22222222B' : Socio (club.getUsuario('22222222B'), 'Pepito López', 'c/direccion2', 666777999, "pepito@gmail.com")})

    def cargarUsuarios(club : Club):
        club.asignarListaUsuarios( {'11111111A' : Usuario ('11111111A','admin', '24/01/2022', True), 
                                '22222222B' : Usuario ('22222222B', 'usuario1', '23/01/2022', False)})

