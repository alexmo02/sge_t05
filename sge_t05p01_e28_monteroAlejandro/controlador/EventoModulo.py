from controlador.SocioModulo import Socio

class Evento: 
    def __init__(self, fechaEvento, fechaMaxInscripcion, localidad, provincia, organizador, kmTotales, precio, listadoSociosApuntados: Socio):
        self._fechaEvento=fechaEvento
        self._fechaMaxInscripcion=fechaMaxInscripcion
        self._localidad=localidad
        self._provincia=provincia
        self._organizador=organizador
        self._kmTotales=kmTotales
        self._precio=precio
        self._listadoSociosApuntados=listadoSociosApuntados