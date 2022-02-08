from modelo.BicicletaModulo import Bicicleta
from modelo.SocioModulo import Socio
from modelo.UsuarioModulo import Usuario
from modelo.ClubModulo import Club
from modelo.EventoModulo import Evento

class Prueba: 
    def cargarSocios(club : Club):
        #self._listaSocios = {'11111111A' : Usuario ("admin", "C/admin", 666777888, "admin@gmail.com")}
        #def __init__(self, usuarioAsociado: Usuario, nombreCompleto, direccion, telefono, correoElectronico, bicicletas: Bicicleta, familia):
        club.asignarListaSocios({'11111111A' : Socio (club.getUsuario('11111111A'), 'Alejandro Montero', 'c/direccion1', 666777888, "alejandro@gmail.com", []),
        '22222222B' : Socio (club.getUsuario('22222222B'), 'Pepito López', 'c/direccion2', 666777999, "pepito@gmail.com", [Bicicleta('30/05/2020', "Canondale", "Modelo1", "Montaña", "Negro", 5, 27, 600, [('30/05/2021', 120, "Cambio de manillar", "delantera")]), Bicicleta('26/06/2020', "Trek", "Modelo2", "Carretera", "Azul", 6, 29, 700, [('30/05/2021', 120, "Cambio de manillar", "delantera")])]), '33333333C' : Socio (club.getUsuario('33333333C'), 'Laura Gómez', 'c/direccion2', 666777999, "pepito@gmail.com", [])})

    def cargarUsuarios(club : Club):
        club.asignarListaUsuarios( {'11111111A' : Usuario ('11111111A','admin', '24/01/2022', True, True), 
                                '22222222B' : Usuario ('22222222B', 'usuario1', '23/01/2022', False, False),
                                '33333333C' : Usuario ('33333333C', 'usuario2', '23/01/2022', False, False)})

    def cargarControlCuotas(club : Club):
        datos_año=({'11111111A' : [2022, club.getSocio('11111111A'), club.getUsuario('11111111A')._corriente_pago, 15, 0, "27-01-2022" ],
        '22222222B' : [2022, club.getSocio('22222222B'), club.getUsuario('22222222B')._corriente_pago, 15, 0, "27-01-2022" ]
        })
        club._controlCuotas=({2022: datos_año})
        
    def cargarEventos(club : Club): 
        eventos=[Evento('25/04/2023', '20/04/2023', "Torrenueva", "Ciudad Real", "TNV", 50, 25, ['22222222B']), Evento('12/03/2022', '10/03/2022', "Martos", "Jaén", "MRT", 5, 1, ['11111111A'] )]
        club._listaEventos=eventos

    '''def cargarBicicletas(socio : Socio):
        bicicletas = [Bicicleta('30/05/2020', "Canondale", "Modelo1", "Montaña", "Negro", 5, 27, 600, [('30/05/2021', 120, "Cambio de manillar", "delantera")]), Bicicleta('26/06/2020', "Trek", "Modelo2", "Carretera", "Azul", 6, 29, 700, [('30/05/2021', 120, "Cambio de manillar", "delantera")])]
        socio._bicicletas=bicicletas'''

