from datetime import date

class VistaUs:
    def inicio(self):
        fdate = date.today().strftime('%d/%m/%Y')
        print("Bienvenido. Hoy es: {}".format(fdate))
        self.mostrarMenu()
        try:
            opc=self.leerOpcionMenu()
            #self._controlador.controlOpciones(opc)
        except Exception as exc:
                self.mostrarError(exc)
        finally:
                self.salir

    def mostrarMenu(self):
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
    
    def leerOpcionMenu(self):
        try:
            opc=int(input("Deme una opción: "))
        except:
            raise Exception("Debes introducir un número entero.")

        if (opc >=0 and opc <=8):
            return opc
        else:
            raise Exception("Debes introducir un número entero entre 0 y 8.")

    def mostrarError(self, exc):
        print("Error!! {}".format(exc))

    def salir(self):
        print("Cerrando aplicación...")