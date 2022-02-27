from datetime import date, datetime

class VistaUs:
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

    def mostrarMenu(self, usuario, fecha):
        print("\nMenú:") 
        print("************************************************")
        print("*              LOS SATANASES DEL               *")
        print("*                INFIERNO APP                  *")
        print("************************************************")
        print("*             Zona de usuarios                 *")
        print("*                Usuario: ",usuario,"          *")
        print("*                Último acc.:",fecha,"      *")
        print("************************************************")
        print("")
        print("====")
        print("1. Ver mis próximos eventos y la lista de inscritos")
        print("2. Ver y apuntarme a eventos abiertos")
        print("3. Ver mis bicicletas")
        print("4. Ver mis reparaciones/mantenimientos")
        print("5. Añadir nueva bicicleta")
        print("6. Añadir reparación/mantenimiento a una de mis bicicletas")
        print("7. Ver mi familia")
        print("8. Ver mi histórico y estado de cuotas")
        print("0. Salir.")
        self.leerOpcionMenu(usuario)
    
    def leerOpcionMenu(self, usuario):
        try:
            opc=int(input("Deme una opción: "))
        except:
            raise Exception("Debes introducir un número entero.")

        if (opc >=0 and opc <=8):
            self._controlador.controlOpciones(opc, usuario)
        else:
            raise Exception("Debes introducir un número entero entre 0 y 8.")

    def mostrarError(self, exc):
        print("Error!! {}".format(exc))

    def salir(self):
        print("Cerrando aplicación...")
        quit()

    def mostrarMisProxEventos(self, listado):
        if(len(listado)>0):
            print("Tus eventos para los próximos días son: ")
            for i in listado: 
                print("Fecha: ", i._fechaEvento)
                print("Fecha Máxima Inscripción: ",i._fechaMaxInscripcion)
                print("Localidad: ", i._localidad)
                print("Provincia: ", i._provincia)
                print("Organización: ", i._organizador)
                print("KM Totales: ", i._kmTotales)
                print("Precio: ", i._precio)
                print("Socios Apuntados: ")
                for j in i._listadoSociosApuntados:
                    socioActual = self._controlador.obtenerSocioActual(j)
                    print("NOMBRE: ", socioActual._nombreCompleto)
                    print("CORREO ELECTRÓNICO: ", socioActual._correoElectronico)
                print("-------------------------------------")
        else: 
            print("No Tienes Eventos para los próximos días")
        print("Pulsa INTRO cuando desees continuar!")
        input()

    def verApuntarEvento(self, listado, usuario):
        if(len(listado)>0):
            print("Los eventos disponibles actualmente son: ")
            j = 0
            while(len(listado)>0):
                if(j==len(listado)):
                    break
                for i in listado: 
                    print("Fecha: ", i._fechaEvento)
                    print("Fecha Máxima Inscripción: ",i._fechaMaxInscripcion)
                    print("Localidad: ", i._localidad)
                    print("Provincia: ", i._provincia)
                    print("Organización: ", i._organizador)
                    print("KM Totales: ", i._kmTotales)
                    print("Precio: ", i._precio)
                    print("¿Deseas apuntarte a este evento (si/no)?")
                    respuesta=input()
                    if(respuesta.lower()=="si"): 
                        if(self._controlador.controlarSociosApuntados(usuario, j, listado)):
                            print("Ya te has apuntado a este evento anteriormente")
                        else: 
                            self._controlador.apuntarSocioEvento(usuario, j, listado)
                            print("Te has apuntado correctamente al evento")
                        respuesta=True
                    j+=1
        else:
            print("No hay eventos disponibles")
        print("Pulsa INTRO cuando desees continuar!")
        input()


    def mostrarBicicletas(self, listado):
        if(len(listado)>0):
            print("Tus bicicletas son: ")
            print()
            for i in listado: 
                print("Fecha Compra: ", i._fechaCompra)
                print("Marca: ", i._marca)
                print("Modelo: ", i._modelo)
                print("Tipo: ", i._tipo)
                print("Color: ", i._color)
                print("Tamaño Cuadro: ", i._tamannoCuadro)
                print("Tamaño Ruedas: ", i._tamannoRuedas)
                print("Precio: ", i._precio)
                print("-------------------------------------")
        else: 
            print("No tienes bicicletas disponibles")
        print("Pulsa INTRO cuando desees continuar!")
        input()

    def mostrarReparaciones(self, listado):
        if(len(listado)>0):
            print("Tus reparaciones/mantenimientos son: ")
            print()
            for i in listado: 
                print("Fecha: ", i._fecha)
                print("Coste: ", i._coste)
                print("Descripción: ", i._descripcion)
                print("Categoria: ", i._categoria)
                print("-------------------------------------")
        else: 
            print("Ninguna de tus bicicletas cuenta con reparaciones")
        print("Pulsa INTRO cuando desees continuar!")
        input()

    def solicitarInfoBicicleta(self, usuario):
        validado = True
        while validado:
            try: 
                print("Introduce la fecha de compra de la bicicleta con formato -> (dia/mes/año - dd/mm/yyyy)")
                fechaCompra = input()
                dato = datetime.strptime(fechaCompra, '%d/%m/%Y')
                validado = False
            except: 
                print("Has introducido la fecha en formato incorrecto, por favor intentalo de nuevo")
        print("Introduce la marca de la bicicleta: ")
        marcaBicicleta = input()
        print("Introduce el modelo de la bicicleta: ")
        modeloBicicleta = input()
        print("Introduce el tipo de la bicicleta: ")
        tipoBicicleta = input()
        print("Introduce el color de la bicicleta:")
        colorBicicleta = input()
        print("Introduce las dimensiones del cuadro de la bicicleta:")
        cuadroBicicleta = float(input())
        print("Introduce las dimensiones de las ruedas de la bicicleta:")
        ruedasBicicleta = input()
        print("Introduce el precio de la bicicleta:")
        precioBicicleta = input()
        self._controlador.insertarBicicleta(fechaCompra, marcaBicicleta, modeloBicicleta, tipoBicicleta, colorBicicleta, cuadroBicicleta, ruedasBicicleta, precioBicicleta, usuario)
        print("Se ha añadido de forma correcta la bicicleta!")
        print("Pulsa INTRO cuando desees continuar!")
        input()

    def agregarReparacion(self, listadoBicicletas, usuario):
        if(len(listadoBicicletas)>0):
            print("Las bicicletas disponibles son: ")
            j = 0 
            while(len(listadoBicicletas)>0):
                if(j == len(listadoBicicletas)):
                    break
                for i in listadoBicicletas:
                    print("Fecha Compra: ", i._fechaCompra)
                    print("Marca: ", i._marca)
                    print("Modelo: ", i._modelo)
                    print("Tipo: ", i._tipo)
                    print("Color: ", i._color)
                    print("Tamaño Cuadro: ", i._tamannoCuadro)
                    print("Tamaño Ruedas: ", i._tamannoRuedas)
                    print("Precio: ", i._precio)
                    print("¿Quieres añadir una reparación a la bicicleta (si/no)?")
                    respuesta = input()
                    if(respuesta.lower() == "si"):
                        self.solicitarInfoReparacion(j, usuario, listadoBicicletas)
                    j+=1
        else:
            print("No hay bicicletas disponibles!")
        print("Pulsa INTRO cuando desees continuar!")
        input()

    def solicitarInfoReparacion(self, j, usuario, listadoBicicletas):
        validado = True
        while validado:
            try: 
                print("Introduce la fecha de la reparación de la bicicleta con formato -> (dia/mes/año - dd/mm/yyyy)")
                fechaReparacion = input()
                dato = datetime.strptime(fechaReparacion, '%d/%m/%Y')
                validado = False
            except: 
                print("Has introducido la fecha en formato incorrecto, por favor intentalo de nuevo")
        validado = True
        while validado: 
            try:
                print("Introduce el coste de la reparación de la bicicleta: ")
                costeReparacion = float(input())
                validado = False
            except:
                print("No has introducido el coste correctamente")
        print("Introduce una breve descripción de la reparación: ")
        descReparacion = input()
        validado = True
        while validado : 
            print("Introduce la categoría perteneciente a la reparación (RUEDAS, FRENOS, ASIENTO, CUADRO, DELANTERA, TRASERA, OTROS)")
            categoriaReparacion = input()
            validado = self._controlador.validarCategoria(categoriaReparacion.upper())
            if validado : 
                print("Debes introducir una de las categorías anteriormente listadas")
        self._controlador.insertarReparacion(j, usuario, listadoBicicletas, fechaReparacion, costeReparacion, descReparacion, categoriaReparacion.upper())
   

    def consultarFamilia(self, familia):
        print("Tus familiares son: ")
        try: 
            print("Pareja: ", self._controlador.obtenerSocioActual(familia["Pareja"])._nombreCompleto)
        except:
            print("Pareja: - ")
        try:
            print("1º Progenitor: ", self._controlador.obtenerSocioActual(familia["Padres"][0])._nombreCompleto)
            print("2º Progenitor: ", self._controlador.obtenerSocioActual(familia["Padres"][1])._nombreCompleto)
        except:
            print("1º Progenitor: -")
            print("2º Progenitor: -")
        
        try:
            if familia["Hijos"]==[]:
                print("Hijo: -")
            else:
                for i in familia["Hijos"]:
                    print("Hijo: ", self._controlador.obtenerSocioActual(i)._nombreCompleto)
        except:
            print("Hijo: -")
        print("Pulsa INTRO cuando desees continuar!")
        input()

    def consultarCuotas(self, cuotas):
        print("La información de tus cuotas es: ")
        print("AÑO   PAGADO   PRECIO    DESCUENTO     FECHA PAGO  ")
        print("---------------------------------------------------")
        for dni, info in cuotas.items():
                if (info[2]==False):
                    print("{:<6}  {:<7} {:<11} {:<11}{:<10}".format(dni,"No" , info[3], info[4], info[5]))
            
        for dni, info in cuotas.items():
            if (info[2]==True):
                print("{:<6}  {:<7} {:<11} {:<11} {:<10}".format(dni, "Si ", info[3], info[4], info[5]))
        print("Pulsa INTRO cuando desees continuar!")
        input()
















