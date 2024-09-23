import numpy as np
import math as math
import time
import sys

sys.setrecursionlimit(2000)  # Aumenta el límite a 2000 (o más si es necesario)

class Ejercicio1:
    """
    Dado 𝑁 números positivos, hallar la suma de todos los valores de 𝑋1 a 𝑋𝑁. Probar con N comprendido en el siguiente rango de representación de números enteros: 0 a 255.Luego probar con N=10000.
    """

    @staticmethod
    def sumaValores():
        lista = []
        cant_N = int(input("Ingrese la cantidad de numeros q ingresara:"))
        for i in range(cant_N):
            N = int(input("Ingrese un numero entre 0 y 256:"))
            if N > 256 and N < 0:
                print("numero fuera de rango")
            else:
                lista.append(N)
        lista = np.array(lista)
        print(lista.sum())

    @staticmethod
    def n10000():
        N = 10000
        X = np.random.randint(1, 101, size= N)

        print(X)
        print(f"Suma de {N} valores: {X.sum()}")

def Ejercicio2_factorial(num:int)->int:
    #Calcular el factorial de un número entero. Una vez codificado el programa, probar ingresando por teclado los siguientes números: 100,1000, 1500.
    if num == 1:
        return 1
    else:
        return Ejercicio2_factorial(num-1)*num

def Ejercicio3_Fibonacci(n:int)->list[int]:
    lista = [0, 1]
    if n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        for i in range(n-2):
            lista.append(lista[-2]+lista[-1])
        return lista
        

def ejercicio4():
    n = input("Ingrese n: ")
    n = int(n)
    e = 1
    print("e = 1 + ")

    for i in range (1, n + 1):
        print(f"+ 1/{i}!")
        e += 1 / math.factorial(i)

def calcular_pi_leibniz(n_terminos):
    pi_aprox = 0
    for i in range(n_terminos):
        pi_aprox += (-1)**i / (2*i + 1)
    return 4 * pi_aprox

def ejercicio5(precision_decimal):
    n_terminos = 1
    while True:
        pi_aprox = calcular_pi_leibniz(n_terminos)
        if round(pi_aprox, precision_decimal) == round(math.pi, precision_decimal):
            return n_terminos, pi_aprox
        n_terminos += 1

if __name__ == '__main__':
    ej = Ejercicio1()
    print()
    num_ejercicio = int(input("Ingrese un el numero de ejercicio:"))
    print('\n')
    if num_ejercicio == 1:
        ej.sumaValores()
    elif num_ejercicio == 2:
        n_factorial = int(input("Ingrese un numero para calcular el factorial:"))
        print(f"el factorial de {n_factorial} es: {Ejercicio2_factorial(n_factorial)}")
    elif num_ejercicio == 3:
        n_serie = int(input("Ingrese el numero N de la serie de fibonachi:"))
        print(f"Serie de fibonachi {Ejercicio3_Fibonacci(n_serie)}")
    elif num_ejercicio == 5:
        n = int(input("Ingrese le numero de presicion: "))
        start_time = time.time()
        terminos_3_dec, pi_3_dec = ejercicio5(1)
        end_time = time.time()

        print(f"Cantidad de términos para {n} dígitos exactos: {terminos_3_dec}")
        print(f"Valor aproximado de pi con {terminos_3_dec} términos: {pi_3_dec}")
        print(f"Tiempo de ejecución: {end_time - start_time} segundos")

    # num = input("Ingrese un numero: ")
    # num = int(num)
    # print(f"El factorial del {num} es: {Ejercicio2_factorial(num=num)}")
    # pass

    # #ejercicio5
    

    #grupo 16