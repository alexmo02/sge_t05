from datetime import date

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

    def muestraSocios(self, lista_socios):
        print("NOMBRES DE LOS SOCIOS")
        for nombre in sorted(lista_socios):
            print("+", nombre)
