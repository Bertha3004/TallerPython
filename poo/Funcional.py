import math

if __name__ == '__main__':

    Suma =lambda x,y:x+y
    print(f"la suma es: {Suma(2,6)}")

    Resta = lambda x, y: x - y
    print(f"la resta es: {Resta(3,4)}")

    Potencia = lambda x: x**2
    print(f"la potencia es: {Potencia(9)}")

    x1 = lambda a, b, c: (-b + math.sqrt(b**2*4*a*c)/2*a)