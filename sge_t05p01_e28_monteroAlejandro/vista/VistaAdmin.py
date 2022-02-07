from datetime import date
from datetime import datetime
from time import strptime
class VistaAd:
    def __init__(self, contr): 
        self._controlador=contr

    def inicio(self):
        fdate = date.today().strftime('%d/%m/%Y')
        print("Bienvenido. Hoy es: {}".format(fdate))
        self.mostrarMenu()
        try:
            opc=self.leerOpcionMenu()
            self._controlador.controlOpciones(opc)
        except Exception as exc:
                self.mostrarError(exc)
        finally:
                self.salir

    def mostrarMenu(self, usuario):
        print("")
        print("************************************************")
        print("*              LOS SATANASES DEL               *")
        print("*                INFIERNO APP                  *")
        print("************************************************")
        print("*            Zona de administración            *")
        print("*                Usuario:",usuario,"           *")
        print("*                Último acc.:                  *")
        print("************************************************")
        print("")
        print("Menú:") 
        print("====")
        print("1. Ver listado completo de socios")
        print("2. Insertar un nuevo socio")
        print("3. Añadir familia a un socio")
        print("4. Ver listado completo de los próximos eventos")
        print("5. Buscar eventos")
        print("6. Insertar un nuevo evento")
        print("7. Ver control de cuotas")
        print("8. Actualizar el control de cuotas")
        print("9. Realizar el control de cuotas")
        print("0. Salir.")
        self.leerOpcionMenu()

    def leerOpcionMenu(self):
        try:
            opc=int(input("Deme una opción: "))
        except:
            raise Exception("Debes introducir un número entero.")

        if (opc >=0 and opc <=9):
            self._controlador.controlOpciones(opc)
        else:
            raise Exception("Debes introducir un número entero entre 0 y 9.")

    def mostrarError(self, exc):
        print("Error!! {}".format(exc))

    def salir(self):
        print("Cerrando aplicación...")
        quit()

    def muestraSocios(self, lista_socios):
        print("NOMBRES DE LOS SOCIOS")
        res1 = sorted(lista_socios, key = lambda s: s.casefold())
        for nombre in res1:
            print("+", nombre)
    
    def insertarSocioUsuario(self):
        validado=False
        while not validado:
            print("Introduce el DNI del socio: ")
            dni=input()
            validado=self._controlador.comprobarDni(dni)
            if not validado:
                print("Ese DNI ya existe, debes introducir uno nuevo")
        print("Introduce la contraseña: ")
        contrasenna=input()
        print("Admin ¿SI/NO?")
        admin=input()
        if (admin.lower=="si"):
            admin=True
        else: admin=False
        print("Introduce el nombre completo del socio: ")
        nombreCompleto=input()
        print("Introduce la dirección del usuario: ")
        direccion=input()
        print("Introduce el teléfono del usuario: ")
        telefono=input()
        print("Introduce el correo electrónico del usuario: ")
        correo=input()
        self._controlador.crearSocioUsuario(dni, contrasenna, admin, nombreCompleto, direccion, telefono, correo)

    def insertarFamiliar(self):
        validado=True
        while validado:
            print("Introduce el DNI del socio al que deseas añadirle familia: ")
            dniSocio = input()
            validado = self._controlador.comprobarDni(dniSocio)
            if not validado: 
                validado = False
        print("Elige una opción para añadir: ")
        print("1. Pareja")
        print("2. Hijos")
        print("3. Padres")
        opcion = 0
        try : opcion = int(input("Introduce una opción: "))
        except : print ("Introduce un número entero, por favor")
        if (opcion >=1 and opcion  <= 3):
            respuesta = self._controlador.agregarFamilia(opcion, dniSocio)
            if respuesta==1:
                print("Este usuario ya tiene una pareja asignada")
            if respuesta==2:
                print("Primero debes asignar una pareja a este cliente")
            if respuesta==3:
                print("El usuario ya tiene dos hijos asociados")
            if respuesta==4:
                print("El usuario ya tiene padres asociados")
        else:print("Introduce un número entero entre 0 y 9.")

    def insertarPareja(self, dniSocio):
        validado = True
        while validado: 
            print("Introduce el DNI de la pareja a insertar (tiene que ser socio/a del club previamente): ")
            dniPareja = input()
            validado = self._controlador.comprobarDni(dniPareja)
            if (dniPareja==dniSocio):
                print("No puedes asignarte a ti mismo como pareja")
                validado = True 
            if not validado: 
                validado = False 
        self._controlador.agregarPareja(dniSocio, dniPareja)

    def insertarHijo(self, dniSocio):
        validado = True
        while validado: 
            print("Introduce el DNI del hijo/a (tiene que ser socio/a del club previamente): ")
            dniHijo = input()
            validado = self._controlador.comprobarDni(dniHijo)
            if (dniHijo==dniSocio):
                print("No puedes ser tu propio hijo: ")
                validado = True
            elif (self._controlador.comprobarPadres(dniHijo)):
                print("Ya tienes unos padres asociados")
            if not validado: 
                validado = False
        self._controlador.agregarHijo(dniSocio, dniHijo)

    def insertarPadres(self, dniUsuario):
        validado = True
        while validado:
            print("Introduce el DNI de uno de tus padres: ")
            dniPareja = input()
            validado = self._controlador.comprobarDni(dniPareja)
            if (not validado):
                if (dniPareja == dniUsuario):
                    print("No puedes ser tu propio padre")
                    validado = True
                elif(self._controlador.comprobarPareja(dniPareja)):
                    print("No tienes pareja, por tanto no es válido")
                    validado = True
                elif(self._controlador.comprobarHijos(dniPareja)):
                    print("Ya tienes 2 hijos asociados")
                if not validado:
                    validado = False
            self._controlador.agregarPadres(dniUsuario, dniPareja)

    def muestraEventos(self, listado):
        print("Eventos para los próximos días: ")
        for i in listado: 
            print("Fecha: ", i._fechaEvento)
            print("Fecha Máxima Inscripción: ",i._fechaMaxInscripcion)
            print("Localidad: ", i._localidad)
            print("Provincia: ", i._provincia)
            print("Organización: ", i._organizador)
            print("KM Totales: ", i._kmTotales)
            print("Precio: ", i._precio)

    def solicitarFechaEvento(self):
        validado = True
        while validado: 
            try: 
                print("Introduce la fecha del Evento con formato -> (dia/mes/año - dd/mm/yyyy)")
                fechaEvento = input()
                dato = datetime.strptime(fechaEvento, '%d/%m/%Y')
                validado = False
            except:
                print("Has introducido la fecha en formato incorrecto, por favor intentalo de nuevo")
        eventoABuscar = self._controlador.realizarBusquedaEventos(fechaEvento)
        for i in eventoABuscar: 
            print("Fecha: ", i._fechaEvento)
            print("Fecha Máxima Inscripción: ",i._fechaMaxInscripcion)
            print("Localidad: ", i._localidad)
            print("Provincia: ", i._provincia)
            print("Organización: ", i._organizador)
            print("KM Totales: ", i._kmTotales)
            print("Precio: ", i._precio)
            print("Socios: ")
            for j in i._listadoSociosApuntados:
                print("DNI: ", j)
            print("-------------------------------------")
    
    def solicitarInfoEvento(self): 
        validado = True
        while validado: 
            try: 
                print("Introduce la fecha en la que se inicia el evento con formato -> (dia/mes/año - dd/mm/yyyy)")
                fechaInicio = input()
                dato = datetime.strptime(fechaInicio, '%d/%m/%Y')
                validado = False
            except: 
                print("Has introducido la fecha en formato incorrecto, por favor intentalo de nuevo")
        validado = True
        while validado: 
            try: 
                print("Introduce la fecha máxima de inscripción para el vento con formato -> (dia/mes/año - dd/mm/yyyy)")
                fechaMaxInscripcion = input()
                dato = datetime.strptime(fechaMaxInscripcion, '%d/%m/%Y')
                if(datetime.strptime(fechaInicio,'%d/%m/%Y'))>=(datetime.strptime(fechaMaxInscripcion, '%d/%m/%Y')):
                    validado = False
                else:
                    print("La fecha máxima de inscripción no puede ser posterior a la fecha del evento, introduce una fecha anterior")
            except:
                print("Has introducido la fecha en formato incorrecto, por favor intentalo de nuevo")
        print("Introduce donde tendrá lugar el evento: ")
        lugar = input()
        print("Introduce la provincia donde tendrá lugar el evento: ")
        provincia = input()
        print("Introduce la organización del evento: ")
        organizacion = input()
        print("Introduce la distancia a recorrer: ")
        distancia = int(input())
        print("Introduce el precio de la inscripción: ")
        precio = int(input())
        sociosEvento = []
        self._controlador.creaEventos(fechaInicio, fechaMaxInscripcion, lugar, provincia, organizacion, distancia, precio, sociosEvento)
        print("Se ha añadido el Evento!")

    def solicitarAnnoContrCuotas(self):
        validado = True
        while validado:
            print("Introduce el año del que quieres obtener información: ")
            try: 
                anno = int(input())
                validado = False
            except: 
                print("Introduce un año correcto")
        return anno

    def muestraControlCuotas(self, cuotas):
        try: 
            print("CONTROL DE CUOTAS")
            print("DNI            AÑO      NOMBRE          PAGADO    PRECIO          DESCUENTO    FECHA PAGO")
            for dni, datos in cuotas.items():
                if (datos[2]==False):
                    print("{:<12} {:<7} {:<20} {:<8} {:<15} {:<10}{:<10}".format(dni, datos[0], datos[1]._nombreCompleto, "No" , datos[3], datos[4], datos[5]))
            for dni, datos in cuotas.items():
                if (datos[2]==True):
                    print("{:<12} {:<7} {:<20} {:<8} {:<15} {:<10} {:<10}".format(dni, datos[0], datos[1]._nombreCompleto, "Si" , datos[3], datos[4], datos[5]))
        except:
            print("No hay datos de dicho año")

    def muestraMensaje(self, string):
        print(string)

    def solicitarPagoCuota(self):
        validado = True
        while validado:
            print("Introduce el DNI del usuario a pagar su cuota: ")
            dni = input()
            validado = self._controlador.comprobarDni(dni)
            if not validado:
                validado = False 
            else: 
                print("No existe ese usuario")
        usuarioExiste = self._controlador.compruebaCuotas()
        if usuarioExiste:
            self.muestraMensaje("Ya hay un control de cuotas para este año")
        else: 
            self._controlador.creaControlCuota()
            self.muestraMensaje("Se ha creado el control de cuotas para ese año con los datos correspondientes")
        cuotaPagada = self._controlador.comprobacionPagado(dni)
        if cuotaPagada:
            print("El usuario ya ha pagado la cuota")
        else: 
            print("Se lleva a cabo el pago")
            print("Debe pagar: ", self._controlador.cantidadAPagar(dni))
            print("Pago realizado!")
            self._controlador.realizarPagoCuota(dni)

















