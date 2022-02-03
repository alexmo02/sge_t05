class Usuario: 
    def __init__(self, dni, contrasenna, ultimoAcceso, es_admin):
        self._dni=dni
        self._contrasenna=contrasenna
        self._ultimoAcceso=ultimoAcceso
        self._es_admin=es_admin
        self._corriente_pago=True

        #hay que hacer que esté al corriente del pago con un booleano
    
    '''def convertirUsuarioAJson(self):
        dictUsuario = {"dni":self._dni, "contrasenna":self._contrasenna, "ultimoAcceso":self._ultimoAcceso, "esAdmin":self._es_admin}
        return dictUsuario'''