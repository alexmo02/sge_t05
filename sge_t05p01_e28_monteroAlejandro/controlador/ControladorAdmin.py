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
        Club.leerJSONUsuarios(self._club)
        Club.leerJSONSocios(self._club)
        Club.leerJSONEventos(self._club)
      
        respuesta = self._club.verificarUsuarioAd(usuario, contrasenna)
        respuesta = self.verificarUltimoAcceso(usuario, contrasenna)

        if(respuesta == 1):
            fechaAcceso = self._club._diccUsuarios[usuario]._ultimoAcceso
            while True: 
                self._vistaAd.mostrarMenu(usuario, fechaAcceso)
        elif(respuesta == 2): 
            self._vistaAd.mostrarError("El usuario y la contraseña no existen")
        elif(respuesta == 3):
            self._vistaAd.mostrarError("Han pasado más de 30 días desde tu último acceso y no tienes la cuota pagada. Contacta con tu administrador!")
        else:
            self._vistaAd.mostrarError("No tienes los permisos para acceder")

    def verificarUltimoAcceso(self, usuario, contrasenna):
        today = datetime.strptime( datetime.today().strftime('%d/%m/%Y') ,"%d/%m/%Y")
        ultimoAcceso = datetime.strptime(self._club._diccUsuarios[usuario]._ultimoAcceso, "%d/%m/%Y")
        tiempoDiscurrido = today - ultimoAcceso 
        if tiempoDiscurrido.days > 30:
            if(self._club._diccUsuarios[usuario]._corriente_pago):
                return 1
            else: return 3
        else:
            return 1

    def listarSocios(self):
        lista = []
        for clave in self._club._diccSocios:
            valor = self._club._diccSocios[clave]
            lista.append(valor._nombreCompleto)
        self._vistaAd.muestraSocios(lista)

    def comprobarDni(self, dni):
        for clave in self._club._diccSocios:
            if clave==dni:
                return False
        return True

    def crearSocioUsuario(self, dni, contrasenna, admin, nombreCompleto, direccion, telefono, correo):
        self._club._diccUsuarios[dni] = Usuario (dni, contrasenna, datetime.today().strftime('%d/%m/%Y'), admin, True)
        self._club._diccSocios[dni] = Socio (self._club.getUsuario(dni), nombreCompleto, direccion, telefono, correo)
        self.agregarControlCuotas(dni)

    def agregarControlCuotas(self, dni):
        anno = datetime.today().strftime('%Y')
        mes = int(datetime.today().strftime('%m'))
        if mes < 7:
            (self._club._controlCuotas[str(anno)])[dni]=[int(anno), dni, self._club.getUsuario(dni)._corriente_pago, 15, 0, datetime.today().strftime('%Y/%m/%d')]
        else:
            (self._club._controlCuotas[str(anno)])[dni]=[int(anno), dni, self._club.getUsuario(dni)._corriente_pago, 8, 0, datetime.today().strftime('%Y/%m/%d')]


    def agregarFamilia(self, opcion, dni):
        if (opcion == 1):
            #comprobamos si este usuario ya tiene una pareja asignada
            if (self._club._diccSocios[dni]._familia["Pareja"]==None and len(self._club._diccSocios[dni]._familia["Padres"])==0):

                self._vistaAd.insertarPareja(dni)
            else:
                return 1
        elif (opcion == 2):
            if (len(self._club._diccSocios[dni]._familia["Padres"])==0): 
                self._vistaAd.insertarHijo(dni)
            else: 
                return 3
        elif (opcion == 3):
            if (self._club._diccSocios[dni]._familia["Pareja"]==None and len(self._club._diccSocios[dni]._familia["Padres"]) < 2):
                self._vistaAd.insertarPadres(dni)
            else:
                return 4
    
    def agregarPareja(self, dniSocio, dniPareja):
        if(self._club._diccSocios[dniPareja]._familia["Pareja"]==None):
            self._club._diccSocios[dniSocio]._familia["Pareja"]=dniPareja
            self._club._diccSocios[dniPareja]._familia["Pareja"]=dniSocio

            if (len(self._club._diccSocios[dniSocio]._familia["Hijos"])>0):
                
                for i in self._club._diccSocios[dniSocio]._familia["Hijos"]:
                    self._club._diccSocios[dniPareja]._familia["Hijos"].append(i)
                
                listado = [dniSocio, dniPareja]

                for i in self._club._diccSocios[dniSocio]._familia["Hijos"]:
                    self._club._diccSocios[i]._familia["Padres"]=[]
                    self._club._diccSocios[i]._familia["Padres"].append(dniPareja)
                    listado.append(i)
                self.actualizarCuotasPadresHijos(listado)

            if (len(self._club._diccSocios[dniPareja]._familia["Hijos"])>0):
                self._club._diccSocios[dniSocio]._familia["Hijos"] = self._club._diccSocios[dniPareja]._familia["Hijos"]
                listado = [dniSocio, dniPareja]

                for i in self._club._diccSocios[dniPareja]._familia["Hijos"]:
                    self._club._diccSocios[i]._familia["Padres"].append(dniSocio)
                    listado.append(i)
                self.actualizarCuotasPadresHijos(listado)
            else: 
                self.actualizarCuotasAgregarPareja(dniSocio, dniPareja)
        else:
            print("Este usuario ya tiene una pareja")

    def actualizarCuotasPadresHijos(self, listado):
        for i in listado:
            self._club._controlCuotas[str(datetime.today().strftime('%Y'))][i][4]=30
            self._club._controlCuotas[str(datetime.today().strftime('%Y'))][i][3]=15*0.7

    def agregarHijo(self, dniSocio, dniHijo):
        dniPareja = self._club.getSocio(self._club._diccSocios[dniSocio]._familia["Pareja"])._usuarioAsociado._dni
        if(dniPareja == dniHijo): 
            print("No puedes asignar a tu pareja como tu hijo")
        else:
            self._club._diccSocios[dniSocio]._familia["Hijos"].append(dniHijo)
            try: 
                dniPareja = self._club.getSocio(self._club._diccSocios[dniSocio]._familia["Pareja"])._usuarioAsociado._dni
                self._club._diccSocios[dniPareja]._familia["Hijos"].append(dniHijo)

                self._club._diccSocios[dniHijo]._familia["Padres"] = [dniSocio, dniPareja]
                self.actualizarCuotasAgregarHijos(dniSocio, dniPareja, dniHijo)
            except: 
                self._club._diccSocios[dniHijo]._familia["Padres"] = [dniSocio]
                self.actualizarcuotasAgregarHijo(dniSocio, dniHijo)

        '''self._club._diccSocios[dniSocio]._familia["Hijos"].append(dniHijo)
        try: 
            dniPareja = self._club.getSocio(self._club._diccSocios[dniSocio]._familia["Pareja"])._usuarioAsociado._dni
            self._club._diccSocios[dniPareja]._familia["Hijos"].append(dniHijo)

            self._club._diccSocios[dniHijo]._familia["Padres"] = [dniSocio, dniPareja]
            self.actualizarCuotasAgregarHijos(dniSocio, dniPareja, dniHijo)
        except: 
            self._club._diccSocios[dniHijo]._familia["Padres"] = [dniSocio]
            self.actualizarcuotasAgregarHijo(dniSocio, dniHijo)'''

    def comprobarPadre(self, dniPareja, dniUsuario):
        if (len(self._club._diccSocios[dniUsuario]._familia["Padres"])==1 and self._club._diccSocios[dniPareja]._familia["Pareja"]!= None):
            return True
        else:
            return False

    def agregarPadres(self, dniHijo, dniSocio):
        try: 
            dniPareja = self._club.getSocio(self._club._diccSocios[dniSocio]._familia["Pareja"])._usuarioAsociado._dni
            self._club._diccSocios[dniSocio]._familia["Hijos"].append(dniHijo)
            self._club._diccSocios[dniPareja]._familia["Hijos"].append(dniHijo)
            #buscamos al hijo y le asignamos los padres
            self._club._diccSocios[dniHijo]._familia["Padres"]=(dniSocio, dniPareja)
            self.actualizarCuotasAgregarHijos(dniSocio, dniPareja, dniHijo)
        except: 
            self._club._diccSocios[dniSocio]._familia["Hijos"].append(dniHijo)
            self._club._diccSocios[dniHijo]._familia["Padres"].append(dniSocio)
            self.actualizarcuotasAgregarHijo(dniSocio, dniHijo)

    def comprobarPadres(self, dniHijo):
        if(len(self._club._diccSocios[dniHijo]._familia["Padres"])<2): return False
        else: return True 

    def comprobarPareja(self, dni):
        if(self._club._diccSocios[dni]._familia["Pareja"])==None: return True
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
    
    def actualizarcuotasAgregarHijo(self, dniSocio, dnihijo):
        self._club._controlCuotas[str(datetime.today().strftime('%Y'))][dniSocio][4]=15
        self._club._controlCuotas[str(datetime.today().strftime('%Y'))][dniSocio][3]=15*0.85
        self._club._controlCuotas[str(datetime.today().strftime('%Y'))][dnihijo][4]=15
        self._club._controlCuotas[str(datetime.today().strftime('%Y'))][dnihijo][3]=15*0.85

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
            self._club._controlCuotas[str(anno)][dni][2]=False
            self._club._controlCuotas[str(anno)][dni][3]=15*(100-self._club._controlCuotas[str(anno)][dni][4])/100
            self._club._controlCuotas[str(anno)][dni][5]=""
    
        for i in self._club._diccUsuarios:
            self._club._diccUsuarios[i]._corriente_pago=False

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
        self._club._controlCuotas[anno][dni][5]=datetime.today().strftime('%d/%m/%Y')

    def controlOpciones(self,opc,usuario):
        if (opc == 0):
            self._club._diccUsuarios[usuario]._ultimoAcceso=datetime.today().strftime('%d/%m/%Y')
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
        else: 
            pass

