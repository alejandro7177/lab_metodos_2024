import math

def func(x: float) -> float:
    return 2 * math.pi * x**3 + 90 * math.pi * x**2 - 45000

def interpolacion_lineal(x_1, x_2, func, error: float = 0.0000000001):
    y_1 = func(x_1)
    y_2 = func(x_2)

    x_3 = (x_1 * y_2 - x_2 * y_1) / (y_2 - y_1)

    if abs(func(x_3)) < error:
        return x_3, func(x_3)
    
    if x_1 < x_2:
        print(f"Intervalo [{x_1}, {x_2}], y_1 = {y_1}, y_2 = {y_2}, x_3 = {x_3}")
    else:
        print(f"Intervalo [{x_2}, {x_1}], y_1 = {y_2}, y_2 = {y_1}, x_3 = {x_3}")

    return interpolacion_lineal(x_2, x_3, func, error)

if __name__ == '__main__':
    resultado = interpolacion_lineal(x_1=10, x_2=15, func=func)
    print(f"Solución aproximada: {resultado}")


