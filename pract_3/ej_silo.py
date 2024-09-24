import math

# Función de interpolación lineal que devuelve una lista de tuplas
def interpolacion_lineal(x_1: float, x_2: float, func, error: float = 1e-10, historial=None)->tuple[list, list]:
    if historial is None:
        historial= []

    y_1 = func(x_1)
    y_2 = func(x_2)

    x_3 = (x_1 * y_2 - x_2 * y_1) / (y_2 - y_1)

    historial.append((x_1, x_2))

    if abs(func(x_3)) < error:
        historial.append((x_1, x_2))
        return historial
    
    return interpolacion_lineal(x_2, x_3, func, error, historial)

if __name__ == '__main__':
    resultado = interpolacion_lineal(x_1=10, x_2=15, func=lambda x: 2*x)
    print(f"Solución aproximada: {resultado}")


