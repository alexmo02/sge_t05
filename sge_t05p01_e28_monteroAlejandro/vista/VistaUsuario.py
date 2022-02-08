from datetime import date

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

    def mostrarMenu(self, usuario):
        print("Menú:") 
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
                print("DNI: ", j)
            print("-------------------------------------")

    '''def verApuntarEvento(self, listado):
        print("Los eventos disponibles actualmente son: ")
        while(len(listado)>0):
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
            if(respuesta.lower=="si"): 
                respuesta=True
            else: 
                respuesta=False'''

    def mostrarBicicletas(self, listado):
        print("Tus bicicletas son: ")
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



















