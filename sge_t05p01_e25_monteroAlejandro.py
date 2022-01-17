import math

class Punto:
    x = 0
    y = 0

    def __init__(self, x=0, y=0):
        self.x=x
        self.y=y

    def __str__(self):
        return "("+str(self.x)+","+str(self.y)+")"

    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            print("{} pertenece al primer cuadrante".format(self))
        elif self.x < 0 and self.y > 0:
            print("{} pertenece al segundo cuadrante".format(self))
        elif self.x < 0 and self.y < 0:
            print("{} pertenece al tercer cuadrante".format(self))
        elif self.x > 0 and self.y < 0:
            print("{} pertenece al cuarto cuadrante".format(self))
        elif self.x != 0 and self.y == 0:
            print("{} se sitúa sobre el eje X".format(self))
        elif self.x == 0 and self.y != 0:
            print("{} se sitúa sobre el eje Y".format(self))
        else:
            print("{} se encuentra sobre el origen".format(self))
    
    def vector(self, p):
        print("El vector entre {} y {} es ({}, {})".format(
            self, p, p.x - self.x, p.y - self.y))

    def distancia(self, p):
        d = math.sqrt( (p.x - self.x)**2 + (p.y - self.y)**2 )
        print("La distancia entre los puntos {} y {} es {}".format(self, p, d))

class Rectangulo: 
    puntoInicial = 0
    puntoFinal = 0

    def __init__(self, puntoInicial=Punto(), puntoFinal=Punto()):
        self.puntoInicial = puntoInicial
        self.puntoFinal = puntoFinal
    
        self.vBase = abs(self.puntoFinal.x - self.puntoInicial.x)
        self.vAltura = abs(self.puntoFinal.y - self.puntoInicial.y)
        self.vArea = self.vBase * self.vAltura
    
    def base(self):
            print("La base del rectángulo es {}".format( self.vBase ) )
    def altura(self):
            print("La altura del rectángulo es {}".format( self.vAltura ) )
    def area(self):
            print("El área del rectángulo es {}".format( self.vArea ) )


puntosValidos = False
while not puntosValidos:
    print("Introduce el valor X del primer punto: ")
    x1=int(input())
    print("Introduce el valor Y del primer punto: ")
    y1=int(input())
    print("Introduce el valor X del segundo punto: ")
    x2=int(input())
    print("Introduce el valor Y del segundo punto: ")
    y2=int(input())

    if(x1==x2 and y1==y2):
        print("NO puedes introducir 2 puntos iguales")
    else: 
        puntosValidos=True
        A = Punto(x1,y1)
        B = Punto(x2,y2)  

opcionSeleccionada = 0

while opcionSeleccionada != 3:
    print("")
    print("Selecciona una operación a realizar: ")
    print("1) Operaciones con puntos")
    print("2) Operaciones con rectángulos")
    print("3) Salir")
        
    opcionSeleccionada = int(input())

    opcionSubmenu = 0

    if opcionSeleccionada == 1:
        print("")
        print("a. Mostrar cuadrante al que pertenecen")
        print("b. Calcular vector")
        print("c. Calcular distancia")

        opcionSubmenu=input()

        if(opcionSubmenu=="a"):
            A.cuadrante()
            B.cuadrante()
        elif(opcionSubmenu=="b"):
            A.vector(B)
            B.vector(A)
        elif(opcionSubmenu=="c"):
            A.distancia(B)
            B.distancia(A)

    elif opcionSeleccionada == 2: 
        print("")
        print("a. Calcular base")
        print("b. Calcular altura")
        print("c. Calcular área")

        opcionSubmenu2=input()

        if(opcionSubmenu2=="a"):
            
        elif(opcionSubmenu2=="b"):

        elif(opcionSubmenu2=="c"):


    elif opcionSeleccionada == 3: 
        print("Hasta pronto!")
    
    elif opcionSeleccionada<1 or opcionSeleccionada>3:
        print("Introduce un número entre el 1 y el 3: ")
