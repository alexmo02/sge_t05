from modelo.SocioModulo import Socio
from modelo.UsuarioModulo import Usuario
from modelo.ClubModulo import Club
from modelo.EventoModulo import Evento

class Prueba: 
    def cargarSocios(club : Club):
        #self._listaSocios = {'11111111A' : Usuario ("admin", "C/admin", 666777888, "admin@gmail.com")}
        #def __init__(self, usuarioAsociado: Usuario, nombreCompleto, direccion, telefono, correoElectronico, bicicletas: Bicicleta, familia):
        club.asignarListaSocios({'11111111A' : Socio (club.getUsuario('11111111A'), 'Alejandro Montero', 'c/direccion1', 666777888, "alejandro@gmail.com"),
        '22222222B' : Socio (club.getUsuario('22222222B'), 'Pepito López', 'c/direccion2', 666777999, "pepito@gmail.com")})

    def cargarUsuarios(club : Club):
        club.asignarListaUsuarios( {'11111111A' : Usuario ('11111111A','admin', '24/01/2022', True), 
                                '22222222B' : Usuario ('22222222B', 'usuario1', '23/01/2022', False)})

    def cargarControlCuotas(club : Club):
        datos_año=({'11111111A' : [2022, club.getSocio('11111111A'), club.getUsuario('11111111A')._corriente_pago, 15, 0, "27-01-2022" ],
        '22222222B' : [2022, club.getSocio('22222222B'), club.getUsuario('22222222B')._corriente_pago, 15, 0, "27-01-2022" ]
        })
        club._controlCuotas=({2022: datos_año,
                                2023:None})
    def cargarEventos(club : Club): 
        eventos=[Evento('20/04/2019', '15/04/2019', "Valdepeñas", "Ciudad Real", "MES", 60, 15, ['11111111A']), Evento('20/04/2022', '15/04/2022', "Membrilla", "Ciudad Real", "ORP", 100, 5, ['11111111A', '12123123X'] )]
        club._listaEventos=eventos
