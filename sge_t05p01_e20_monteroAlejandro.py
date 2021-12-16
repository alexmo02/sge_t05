def sumar(num1,num2):
    suma = num1 + num2
    return suma

def restar(num1,num2):
    resta = num1 - num2
    return resta

def multiplicar(num1,num2):
    multiplicacion = num1 * num2
    return multiplicacion

def dividir(num1,num2):
    division = float(num1 / num2)
    return division
    
def realizaPotencia(num1,num2):
    potencia = num1 ** num2
    return potencia


ejecutando=True
while ejecutando:
    try:
        num1 = int(input("Introduce el primer número: "))
        num2 = int(input("Introduce el segundo número: ")) 

        opcionElegida = 0

        while opcionElegida != 6:
            print("""
            Seleccione la operación que desea realizar
        
            1) SUMAR
            2) RESTAR
            3) MULTIPLICAR
            4) DIVIDIR
            5) CALCULAR POTENCIA
            6) SALIR 
            """)

            opcionElegida = int(input())

            if opcionElegida == 1:
                print(" ")
                print("El resultado de la suma es: ",sumar(num1,num2))
            elif opcionElegida == 2: 
                print(" ")
                print("El resultado de la resta es: ",restar(num1,num2))
            elif opcionElegida == 3: 
                print(" ")
                print("El resultado de la multiplicación es: ",multiplicar(num1,num2))    
            elif opcionElegida == 4: 
                print(" ")
                print("El resultado de la división es: ",dividir(num1,num2))    
            elif opcionElegida == 5: 
                print(" ")
                print("El resultado de la potencia es: ",realizaPotencia(num1,num2)) 
            elif opcionElegida == 6: 
                print("Hasta pronto!")
                ejecutando=False
             
    except ValueError: 
        print("Debes introducir un número entero o real")


    






    