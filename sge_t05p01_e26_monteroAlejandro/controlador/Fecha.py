import os
from datetime import datetime

class Fecha: 
    def __init__(self, d=0, m=0, a=0):
        self._dia = d
        self._mes = m
        self._anno= a

    @classmethod
    def fecha_actual(self):
        f_actual = datetime.now()
        return self(f_actual.day, f_actual.month, f_actual.year)

    @classmethod
    def fecha_validar(self, d=0, m=0, a=0):
        try:
            datetime(a, m, d)
            return self(d, m, a)
        except ValueError:
            raise ValueError("Fecha no válida.")
    
    def __str__(self):
        return "{:02d}/{:02d}/{:04d}".format(self._dia, self._mes, self._anno)

