from modelo.SocioModulo import Socio
from modelo.EventoModulo import Evento

class Club:
    def __init__(self, nombreClub, cif, sedeSocial, listaSocios: Socio, listaEventos: Evento, saldototal, controlCuotas):
        self._nombreClub=nombreClub
        self._cif=cif
        self._sedeSocial=sedeSocial
        self._listaSocios=listaSocios
        self._listaEventos=listaEventos
        self._saldoTotal=saldototal
        self._controlCuotas=controlCuotas