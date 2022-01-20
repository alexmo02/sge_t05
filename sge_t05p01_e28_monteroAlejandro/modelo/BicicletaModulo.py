from modelo.ReparacionModulo import Reparacion


from modelo.ReparacionModulo import Reparacion

class Bicicleta:
    def __init__(self, fechaCompra, marca, modelo, tipo, color, tamannoCuadro, tamannoRuedas, precio, listaReparaciones: Reparacion):
        self._fechaCompra=fechaCompra
        self._marca=marca
        self._modelo=modelo
        self._tipo=tipo
        self._color=color
        self._tamannoCuadro=tamannoCuadro
        self._tamannoRuedas=tamannoRuedas
        self._precio=precio
        self._listaReparaciones=listaReparaciones
