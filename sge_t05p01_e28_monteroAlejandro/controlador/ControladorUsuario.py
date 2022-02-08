from modelo.Prueba import Prueba
from vista.VistaUsuario import VistaUs
from modelo.ClubModulo import Club
from datetime import datetime

class ControladorUs:
    def __init__(self, club : Club, usuario, contrasenna):
        self._club=club
        self._vistaUs=VistaUs(self)
        self.inicio(usuario, contrasenna)
    
    def inicio(self, usuario, contrasenna):
        Prueba.cargarUsuarios(self._club)
        Prueba.cargarSocios(self._club)
        Prueba.cargarEventos(self._club)
        #Prueba.cargarBicicletas(self._club._diccSocios[usuario])

        if(self._club.verificarUsuarioUs(usuario, contrasenna)):
            while True: 
                self._vistaUs.mostrarMenu(usuario)
        else:
            self._vistaUs.mostrarError("El usuario y la contraseña no existen")

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

    #algo para el segundo apartado
    def apuntarSocioEvento(self, usuario, posicion):
        self._club._listaEventos[posicion]._listadoSociosApuntados.append(usuario)
        
    def obtenerBicicletas(self, usuario):
        listadoBicicletas = []
        for i in self._club._diccSocios[usuario]._bicicletas:
            listadoBicicletas.append(i)
        return listadoBicicletas


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
 

    '''def realizarBusquedaUsuario(self, usuario):
        listado = []
        for i in self._club._listaEventos:
            if(i._listadoSocios[usuario]==usuario):
                listado.append(i)
        return listado'''