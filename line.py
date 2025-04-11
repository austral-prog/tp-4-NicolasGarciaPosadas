import math

# Entrada de datos
def line():
    a = float(input("Ingrese el coeficiente A: "))
    b = float(input("Ingrese el coeficiente B: "))
    x1 = float(input("Ingrese el coeficiente X1: "))
    x2 = float(input("Ingrese el coeficiente X2: "))

# Cálculo de Y1 y Y2 usando la ecuación Y = aX + b
    y1 = a * x1 + b
    y2 = a * x2 + b

# Cálculo de la distancia entre dos puntos en el plano
    distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Salida de resultados
    print(f"El coeficiente A de su ecuación de la recta es: {a}")
    print(f"El coeficiente B de su ecuación de la recta es: {b}")
    print(f"El coeficiente X1 de su ecuación de la recta es: {x1}")
    print(f"El coeficiente X2 de su ecuación de la recta es: {x2}")

    print(f"\nPara la siguiente ecuación:\n\tY = {a}X + {b}")
    print(f"\nDados los siguientes puntos:\n\tP1 ({x1}, {y1})\n\tP2 ({x2}, {y2})")
    print(f"\nLa distancia entre ellos es: {distancia}")
    











#Ingrese el coeficiente A: 2.3
#Ingrese el coeficiente B: -4
#Ingrese el coeficiente X1: 50
#Ingrese el coeficiente X2: -32.9
#El coeficiente A de su ecuación de la recta es: 2.3
#El coeficiente B de su ecuación de la recta es: -4.0
#El coeficiente X1 de su ecuación de la recta es: 50.0
#El coeficiente X2 de su ecuación de la recta es: -32.9

#Para la siguiente ecuación:
#	Y = 2.3X + -4.0

#Dados los siguientes puntos:
#	P1 (50.0, 110.99999999999999)
#	P2 (-32.9, -79.66999999999999)
#La distancia entre ellos es: 207.9121422620622
