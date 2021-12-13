import statistics
numero=1
my_list = []
while numero > 0:
    try:
        numero = int(input("Introduce un número: "))
        if numero > 0:
            my_list.append(numero)
            mean = statistics.mean(my_list)
        else:
            print('La media de los números introducidos es: ' + str(mean))
    except ValueError:
        print("Eso no es un número")
