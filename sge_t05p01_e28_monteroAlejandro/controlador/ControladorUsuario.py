from modelo.Prueba import Prueba
from vista.VistaUsuario import VistaUs
from modelo.ClubModulo import Club
from datetime import date, datetime

class ControladorUs:
    def __init__(self, club : Club, usuario, contrasenna):
        self._club=club
        self._vistaUs=VistaUs(self)
        self.inicio(usuario, contrasenna)
    
    def inicio(self, usuario, contrasenna):
        Prueba.cargarUsuarios(self._club)
        Prueba.cargarSocios(self._club)
        Prueba.cargarEventos(self._club)
        
        resultado = self._club.verificarUsuarioUs(usuario, contrasenna)

        if(resultado==1):
            while True: 
                self._vistaUs.mostrarMenu(usuario)
        elif(resultado==2):
            self._vistaUs.mostrarError("El usuario o la contraseña no existen")
        else:
            self._vistaUs.mostrarError("Este usuario no tiene permiso para acceder")

    def obtenerEventosUsuario(self, usuario):
        listado = []
        for i in self._club._listaEventos:
            fecha = datetime.today().strftime('%d/%m/%Y')
            if(datetime.strptime(i._fechaEvento,'%d/%m/%Y'))>(datetime.today().strptime(fecha, '%d/%m/%Y')):
                for j in i._listadoSociosApuntados:
                    if(j==usuario):
                        listado.append(i)
        return listado

    def obtenerEventosParaTodos(self):
        listado = []
        for i in self._club._listaEventos:
            fecha = datetime.today().strftime('%d/%m/%Y')
            if(datetime.strptime(i._fechaEvento,'%d/%m/%Y'))>(datetime.today().strptime(fecha, '%d/%m/%Y')):
                listado.append(i)
        return listado

    def controlarSociosApuntados(self, usuario, j, listado):
        socioApuntado = False
        for i in listado[j]._listadoSociosApuntados:
            if i == usuario: 
                socioApuntado = True
        return socioApuntado

    #algo para el segundo apartado
    def apuntarSocioEvento(self, usuario, posicion, eventosDisponibles):
        eventosDisponibles[posicion]._listadoSociosApuntados.append(usuario)
        eventosFinalizados = []
        for i in self._club._listaEventos:
            fecha = datetime.today().strftime('%d/%m/%Y')
            if(datetime.strptime(i._fechaEvento, '%d/%m/%Y')) < (datetime.today().strptime(fecha, '%d/%m/%Y')):
                eventosFinalizados.append(i)
        eventos = []
        for i in eventosFinalizados:
            eventos.append(i)
        for i in eventosDisponibles:
            eventos.append(i)
        self._club._listaEventos = eventos
        
    def obtenerBicicletas(self, usuario):
        listadoBicicletas = []
        for i in self._club._diccSocios[usuario]._bicicletas:
            listadoBicicletas.append(i)
        return listadoBicicletas

    def obtenerReparaciones(self, usuario):
        listadoReparaciones = []
        for i in self._club._diccSocios[usuario]._bicicletas:
            for j in i._listaReparaciones:
                listadoReparaciones.append(j)
        return listadoReparaciones


    def controlOpciones(self,opc, usuario):
        if (opc == 0):
            self._vistaUs.salir()
        elif (opc == 1):
            listado = self.obtenerEventosUsuario(usuario)
            self._vistaUs.mostrarMisProxEventos(listado)
        elif (opc == 2):
            listado = self.obtenerEventosParaTodos()
            self._vistaUs.verApuntarEvento(listado, usuario)
        elif (opc == 3):
            listado = self.obtenerBicicletas(usuario)
            self._vistaUs.mostrarBicicletas(listado)
        elif (opc == 4):
            listado = self.obtenerReparaciones(usuario)
            self._vistaUs.mostrarReparaciones(listado)
 

    '''def realizarBusquedaUsuario(self, usuario):
        listado = []
        for i in self._club._listaEventos:
            if(i._listadoSocios[usuario]==usuario):
                listado.append(i)
        return listado'''