import json

from modelo.SocioModulo import Socio
from modelo.EventoModulo import Evento
from modelo.UsuarioModulo import Usuario
from modelo.BicicletaModulo import Bicicleta
from modelo.ReparacionModulo import Reparacion
from datetime import datetime, time
class Club:
    def __init__(self, nombreClub, cif, sedeSocial=None, saldoTotal=0, controlCuotas={}):
        self._nombreClub=nombreClub
        self._cif=cif
        self._sedeSocial=sedeSocial
        self._diccSocios={}
        self._listaEventos=[]
        self._saldoTotal=saldoTotal
        self._controlCuotas=controlCuotas
        self._diccUsuarios={}

    def asignarListaSocios(self, diccionarioSocios):
        self._diccSocios=diccionarioSocios

    def asignarListaUsuarios(self, diccionarioUsuarios):
        self._diccUsuarios=diccionarioUsuarios

    def getUsuario(self, dni):
        return self._diccUsuarios[dni]

    def getSocio(self, dni):
        return self._diccSocios[dni]

    def verificarUsuarioAdmin(self, argumentos):
        if len(argumentos)==6:
            if argumentos[5]=="-A" :
                return True               
        if len(argumentos)==5:
            return False

    def verificarUsuarioUsuar(self, argumentos):
        if len(argumentos) == 5: 
            return True

    def verificarUsuarioAd(self, usuario : Usuario, contrasenna):
        try:
            if(self._diccUsuarios[usuario]):
                usuario=self._diccUsuarios[usuario]
                if(contrasenna==usuario._contrasenna):
                    if(usuario._es_admin):
                        today=datetime.strptime( datetime.today().strftime('%d/%m/%Y') ,"%d/%m/%Y")
                        ult_acceso=datetime.strptime(self._diccUsuarios[usuario._dni]._ultimoAcceso, "%d/%m/%Y")
                        diferencia = today-ult_acceso
                        if diferencia.days<30:
                            if(self._diccUsuarios[usuario._dni]._corriente_pago):
                                return 1
                            else: return 3
                        else:
                            return 3
                    else:
                        return 4
                else:
                    return 2
            else: 
                return 2
        except: 
            return 2
    
    def verificarUsuarioUs(self, usuario : Usuario, contrasenna):
        try:
            if(self._diccUsuarios[usuario]):
                usuario=self._diccUsuarios[usuario]
                if(contrasenna==usuario._contrasenna):
                    today=datetime.strptime( datetime.today().strftime('%d/%m/%Y') ,"%d/%m/%Y")
                    ult_acceso=datetime.strptime(self._diccUsuarios[usuario._dni]._ultimoAcceso, "%d/%m/%Y")
                    diferencia = today-ult_acceso
                    if diferencia.days<30:
                        if(self._diccUsuarios[usuario._dni]._corriente_pago):
                            return 1
                        else: return 4
                    else:
                        return 3
                else:
                    return 2
            else: 
                return 2
        except: 
            return 2

    def guardarJSONUsuarios(rutaFich, coleccion):
        with open(rutaFich, 'w') as f:
            json.dump(coleccion, f, indent=2)
    
    def leerJSONUsuarios(self):
        with open("usuario.json", 'r') as f:
            cadjson=json.load(f)
        for i in cadjson:
            self._diccUsuarios[i["_dni"]]=(Usuario(i["_dni"], i["_contrasenna"], i["_ultimoAcceso"], i["_es_admin"], i["_corriente_pago"]))

    def leerJSONSocios(self):
        with open("socio.json", 'r') as f:
            cadjson=json.load(f)
        for i in cadjson:
            #creamos la lista de bicicletas
            listabici=[]
            for e in i["_bicicletas"]:
                #creamos la lista de reparaciones
                listarep=[]
                for c in e["_listaReparaciones"]:
                    listarep.append(Reparacion(c["_fecha"], c["_coste"], c["_descripcion"],c["_categoria"]))
                listabici.append(Bicicleta(e["_fechaCompra"], e["_marca"], e["_modelo"],e["_tipo"],e["_color"],e["_tamannoCuadro"],e["_tamannoRuedas"],e["_precio"],listarep))
            self._diccSocios[i["_usuarioAsociado"]]=(Socio(self.getUsuario(i["_usuarioAsociado"]), i["_nombreCompleto"], i["_direccion"], i["_telefono"], i["_correoElectronico"], listabici, i["_familia"]))

    def leerJSONEventos(self):
        with open("evento.json", 'r') as f:
            cadjson=json.load(f)
        for i in cadjson:
            self._listaEventos.append(Evento(i["_fechaEvento"],i["_fechaMaxInscripcion"],i["_localidad"],i["_provincia"],i["_organizador"],i["_kmTotales"],i["_precio"],i["_listadoSociosApuntados"]))
    
    def guardarJSONSocios(rutaFich, coleccion):
        with open(rutaFich, 'w') as f:
            json.dump(coleccion, f, indent=2)
    
    def guardarJSONClub(rutaFich, coleccion):
        with open(rutaFich, 'w') as f:
            json.dump(coleccion, f, indent=2)
    
    def guardarJSONEventos(rutaFich, coleccion):
        with open(rutaFich, 'w') as f:
            json.dump(coleccion, f, indent=2)
    
    def guardarJSONBicicletas(rutaFich, coleccion):
        with open(rutaFich, 'w') as f:
            json.dump(coleccion, f, indent=2)
    
    
   
