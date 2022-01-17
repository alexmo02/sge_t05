clientes= {}
clientes['11111111D']=['Alejandro','Montero González','Calle Velázquez 5', 666777888, 'alejandro@gmail.com', True]

opcionSeleccionada = 0

while opcionSeleccionada != 7:
    try:
        
        print("Selecciona una operación a realizar: ")
        print("1) Añadir cliente")
        print("2) Eliminar cliente")
        print("3) Mostrar cliente")
        print("4) Listar todos los clientes")
        print("5) Listar clientes preferentes")
        print("6) Ordenar por apellidos")
        print("7) Terminar ")
        
        opcionSeleccionada = int(input())

        if opcionSeleccionada == 1:
            print("Añadimos un nuevo cliente")
            dniCorrecto=False
            while not dniCorrecto:
                print("Introduce el DNI: ")
                dni=input()
                
                if dni in clientes:
                    print("Ese DNI ya existe en nuestra base de datos") 
                    
                else:
                    dniCorrecto=True

            print("Introduce el nombre: ")
            nombre=input()
            print("Introduce el apellido: ")
            apellido=input()
            print("Introduce la direccion: ")
            direccion=input()
            print("Introduce el telefono: ")
            telefono=int(input())
            print("Introduce el correo: ")
            correo=input()
            print("Introduce si es preferente o no: ")
            prioritario=bool(input())
            clientes[dni]=[apellido, nombre, direccion, telefono, correo, prioritario]

            
        elif opcionSeleccionada == 2: 
            
            dniCorrecto=False
            while not dniCorrecto:
                print("Introduce el DNI del cliente a eliminar: ")
                dniEliminar=input()
                if dniEliminar in clientes:
                    print("El DNI existe por lo que será eliminado")
                    dniCorrecto=True
                    del clientes[dniEliminar]
                else:
                    print("El DNI no existe")
                    
        elif opcionSeleccionada == 3: 
            print("Introduce el DNI del cliente: ")
            dni=input()
            print("Los datos del cliente son: ")
            print("Nombre: ", clientes[dni][0])
            print("Apellidos: ", clientes[dni][1])
            print("Direccion: ", clientes[dni][2])
            print("Telefono: ", clientes[dni][3])
            print("Correo: ", clientes[dni][4])
            print("Preferente: ", clientes[dni][5])
            print("")
 
        elif opcionSeleccionada == 4: 
            print("Clientes Almacenados: ")
            for a, b in clientes.items():
                print("DNI: ", a, " Datos: ", b)
            
        elif opcionSeleccionada == 5: 
            print("Estos son todos los clientes que tenemos almacenados como PREFERENTES: ")
            for a, b in clientes.items():
                if b[5]==True:
                    print("DNI: ", a, " Datos: ", b)

        elif opcionSeleccionada == 6: 
            print("Estos son todos los clientes que tenemos almacenados (ordenados por APELLIDO): ")
            listaClientesApellido = sorted(clientes.items(), key=lambda item:item[1][1])
            print(listaClientesApellido)
            
        elif opcionSeleccionada == 7: 
            print("Hasta pronto!")
        
        elif opcionSeleccionada<1 or opcionSeleccionada>7:
            print("Introduce un número entre el 1 y el 7: ")
        
    except ValueError: 
        print("No has introducido un número! Debes introducir un número entre el 1 y el 7: ")