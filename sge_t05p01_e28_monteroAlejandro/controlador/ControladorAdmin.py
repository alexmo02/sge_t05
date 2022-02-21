from re import S
from modelo.Prueba import Prueba
from modelo.UsuarioModulo import Usuario
from vista.VistaAdmin import VistaAd
from modelo.ClubModulo import Club
from modelo.PersistenciaJSON import Persistencia
from modelo.SocioModulo import Socio
from modelo.EventoModulo import Evento
from datetime import datetime

class ControladorAd:
    def __init__(self, club : Club, usuario, contrasenna):
        self._club=club
        self._vistaAd=VistaAd(self)
        self.inicio(usuario, contrasenna)
    
    def inicio(self, usuario, contrasenna):
        '''Prueba.cargarUsuarios(self._club)
        Prueba.cargarSocios(self._club)
        Prueba.cargarControlCuotas(self._club)
        Prueba.cargarEventos(self._club)'''
        Club.leerJSONUsuarios(self._club)
        Club.leerJSONSocios(self._club)
        Club.leerJSONEventos(self._club)
      
        respuesta = self._club.verificarUsuarioAd(usuario, contrasenna)
        if(respuesta == 1):
            while True: 
                self._vistaAd.mostrarMenu(usuario)
        elif(respuesta == 2): 
            self._vistaAd.mostrarError("El usuario y la contraseña no existen")
        else:
            self._vistaAd.mostrarError("No tienes los permisos para acceder")

    def listarSocios(self):
        lista = []
        for clave in self._club._diccSocios:
            valor = self._club._diccSocios[clave]
            lista.append(valor._nombreCompleto)
        self._vistaAd.muestraSocios(lista)

    #esta comprobación en el modelo
    def comprobarDni(self, dni):
        for clave in self._club._diccSocios:
            if clave==dni:
                return False
        return True

    def crearSocioUsuario(self, dni, contrasenna, admin, nombreCompleto, direccion, telefono, correo):
        self._club._diccUsuarios[dni] = Usuario (dni, contrasenna, datetime.today().strftime('%Y/%m/%d'), admin, True)
        self._club._diccSocios[dni] = Socio (dni, nombreCompleto, direccion, telefono, correo)

        self.agregarControlCuotas(dni)

    def agregarControlCuotas(self, dni):
        (self._club._controlCuotas["2022"])[dni]=[2022, dni, self._club.getUsuario(dni)._corriente_pago, 15, 0, datetime.today().strftime('%Y/%m/%d')]


    def agregarFamilia(self, opcion, dni):
        if (opcion == 1):
            #comprobamos si este usuario ya tiene una pareja asignada
            if(self._club._diccSocios[dni]._familia["Pareja"]==None and len(self._club._diccSocios[dni]._familia["Padres"])==0):
                self._vistaAd.insertarPareja(dni)
            else:
                return 1
        elif (opcion == 2):
            if ( self._club._diccSocios[dni]._familia["Pareja"]==None): return 2
            
            elif(len(self._club._diccSocios[dni]._familia["Hijos"])<=1  and len(self._club._diccSocios[dni]._familia["Padres"])==0):
                self._vistaAd.insertarHijo(dni)
            else: return 3
        elif (opcion ==3):
            if (self._club._diccSocios[dni]._familia["Pareja"]==None and len(self._club._diccSocios[dni]._familia["Padres"])==0):
                self._vistaAd.insertarPadres(dni)
            else:
                return 4
    
    def agregarPareja(self, dniSocio, dniPareja):
        self._club._diccSocios[dniSocio]._familia["Pareja"]=self._club._diccSocios[dniPareja]
        self._club._diccSocios[dniPareja]._familia["Pareja"]=self._club._diccSocios[dniSocio]

        self.actualizarCuotasAgregarPareja(dniSocio, dniPareja)

    def agregarHijo(self, dniSocio, dniHijo):
        self._club._diccSocios[dniSocio]._familia["Hijos"].append(self._club._diccSocios[dniHijo])
        dniPareja=self._club._diccSocios[dniSocio]._familia["Pareja"]._usuarioAsociado._dni
        self._club._diccSocios[dniPareja]._familia["Hijos"].append(self._club._diccSocios[dniHijo])

        self._club._diccSocios[dniHijo]._familia["Padres"]=(self._club._diccSocios[dniSocio], self._club._diccSocios[dniPareja])
        self.actualizarCuotasAgregarHijos(dniSocio, dniPareja, dniHijo)

    def agregarPadres(self, dniHijo, dniSocio):
        dniPareja=self._club._diccSocios[dniSocio]._familia["Pareja"]._usuarioAsociado._dni
        self._club._diccSocios[dniSocio]._familia["Hijos"].append(self._club._diccSocios[dniHijo])
        self._club._diccSocios[dniPareja]._familia["Hijos".append(self._club._diccSocios[dniHijo])]

        self._club._diccSocios[dniHijo]._familia["Padres"]=(self._club._diccSocios[dniSocio], self._club._diccSocios[dniPareja])
        self.actualizarCuotasAgregarHijos(dniSocio, dniPareja, dniHijo)

    def comprobarPadres(self, dniHijo):
        if(len(self._club._diccSocios[dniHijo]._familia["Padres"])==0): return False
        else: return True 

    def comprobarPareja(self, dni):
        if(len(self._club._diccSocios[dni]._familia["Padres"])==None): return True
        else: return False 
    
    def comprobarHijos(self, dni): 
        if(len(self._club._diccSocios[dni]._familia["Hijos"])<=1): return False
        else: return True 

    def actualizarCuotasAgregarPareja(self, dniSocio, dniPareja):
        self._club._controlCuotas[str(datetime.today().strftime('%Y'))][dniSocio][4]=10
        self._club._controlCuotas[str(datetime.today().strftime('%Y'))][dniSocio][3]=15*0,9
        self._club._controlCuotas[str(datetime.today().strftime('%Y'))][dniPareja][4]=10
        self._club._controlCuotas[str(datetime.today().strftime('%Y'))][dniPareja][3]=15*0,9

    def actualizarCuotasAgregarHijos(self, dniSocio, dniPareja, dniHijo): 
        self._club._controlCuotas[str(datetime.today().strftime('%Y'))][dniSocio][4]=30
        self._club._controlCuotas[str(datetime.today().strftime('%Y'))][dniSocio][3]=15*0,7 
        self._club._controlCuotas[str(datetime.today().strftime('%Y'))][dniPareja][4]=30
        self._club._controlCuotas[str(datetime.today().strftime('%Y'))][dniPareja][3]=15*0,7
        self._club._controlCuotas[str(datetime.today().strftime('%Y'))][dniHijo][4]=30
        self._club._controlCuotas[str(datetime.today().strftime('%Y'))][dniHijo][3]=15*0,7

    def obtenerEventos(self):
        for i in self._club._listaEventos:
            listado = []
            fecha = datetime.today().strftime('%d/%m/%Y')
            if(datetime.strptime(i._fechaEvento,'%d/%m/%Y'))>(datetime.today().strptime(fecha, '%d/%m/%Y')):
                listado.append(i)
        return listado

    def realizarBusquedaEventos(self, fecha):
        listado = []
        for i in self._club._listaEventos:
            if(datetime.strptime(i._fechaEvento, '%d/%m/%Y'))==(datetime.strptime(fecha,'%d/%m/%Y')):
                listado.append(i)
        return listado
    
    def creaEventos(self, fechaInicio, fechaInscrip, lugar, provincia, organizacion, distancia, precio, socios): 
        self._club._listaEventos.append(Evento(fechaInicio, fechaInscrip, lugar, provincia, organizacion, distancia, precio, socios))

    def obtenerCuota(self, anno):
        try: 
            return self._club._controlCuotas[anno]
        except:
            return ""

    def compruebaCuotas(self):
        anno = str(datetime.today().strftime('%Y'))
        try: 
            datos=self._club._controlCuotas[anno]
            return True 
        except:
            return False

    def creaControlCuota(self):
        anno = int(datetime.today().strftime('%Y'))
        controlCuota = self._club._controlCuotas[str(anno-1)]
        self._club._controlCuotas[str(anno)] = controlCuota
        for dni in self._club._controlCuotas[str(anno)]:
            self._club._controlCuotas[str(anno)][dni][2] = False
    
    def comprobacionPagado(self, dni):
        anno = str(datetime.today().strftime('%Y'))
        if self._club._controlCuotas[anno][dni][2]:
            return True
        else: return False

    def cantidadAPagar(self, dni):
        anno = str(datetime.today().strftime('%Y'))
        return self._club._controlCuotas[anno][dni][3]

    def realizarPagoCuota(self, dni):
        anno = str(datetime.today().strftime('%Y'))
        self._club.getUsuario(dni)._corriente_pago = True
        self._club._controlCuotas[anno][dni][2] = self._club.getUsuario(dni)._corriente_pago

    def controlOpciones(self,opc):
        if (opc == 0):
            Persistencia.guardarDatos(self._club)
            self._vistaAd.salir()
        elif (opc == 1):
            self.listarSocios()
        elif (opc == 2):
            self._vistaAd.insertarSocioUsuario()
        elif (opc == 3):
            self._vistaAd.insertarFamiliar()
        elif (opc == 4):
            listado = self.obtenerEventos()
            self._vistaAd.muestraEventos(listado)
        elif (opc == 5):
            self._vistaAd.solicitarFechaEvento()
        elif (opc == 6):
            self._vistaAd.solicitarInfoEvento()
        elif (opc == 7):
            anno = self._vistaAd.solicitarAnnoContrCuotas()
            cuotas = self.obtenerCuota(str(anno))
            self._vistaAd.muestraControlCuotas(cuotas, self._club)
        elif (opc == 8):
            existe = self.compruebaCuotas()
            if existe: 
                self._vistaAd.muestraMensaje("Ya hay un control de cuotas para este año")
            else: 
                self.creaControlCuota()
                self._vistaAd.muestraMensaje("Se ha creado el control de cuotas para ese año con los datos correspondientes")
        elif (opc == 9):
            self._vistaAd.solicitarPagoCuota()
            
    '''def cargarSocios(club : Club):
        #self._listaSocios = {'11111111A' : Usuario ("admin", "C/admin", 666777888, "admin@gmail.com")}
        #def __init__(self, usuarioAsociado: Usuario, nombreCompleto, direccion, telefono, correoElectronico, bicicletas: Bicicleta, _familia):
        club.asignarListaSocios({'11111111A' : Socio (club.getUsuario('11111111A'), 'Alejandro Montero', 'c/direccion1', 666777888, "alejandro@gmail.com"),
        '22222222B' : Socio (club.getUsuario('22222222B'), 'Pepito López', 'c/direccion2', 666777999, "pepito@gmail.com")})

    def cargarUsuarios(club : Club):
        listaUsuarios = Persistencia.leerJSON("carpetaJSON/usuario.json")
        for usuario in listaUsuarios:

        club.asignarListaUsuarios()'''



