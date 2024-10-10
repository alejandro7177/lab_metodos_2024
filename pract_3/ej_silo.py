import math

# Función de interpolación lineal que devuelve una lista de tuplas
def interpolacion_lineal(x_1: float, x_2: float, func, error: float = 1e-10, historial=None) -> list:
    if historial is None:
        historial = []
        historial.append(x_1)
    
    # Evaluar la función en los puntos x_1 y x_2
    y_1 = func(x_1)
    y_2 = func(x_2)

    # Calcular el nuevo punto x_3 usando interpolación lineal
    x_3 = (x_1 * y_2 - x_2 * y_1) / (y_2 - y_1)

    # Agregar el intervalo actual (x_1, x_2) al historial
    historial.append(x_3)  # Agregamos x_3 al historial

    # Condición de parada: si la función en x_3 es suficientemente pequeña, terminamos
    if abs(func(x_3)) < error:      
        return historial
    
    # Si la función cambia de signo entre x_1 y x_3, usamos ese intervalo, de lo contrario, usamos x_3 y x_2

    return interpolacion_lineal(x_1, x_3, func, error, historial)

if __name__ == '__main__':
    # Cambiamos la función a una no lineal con una raíz
    resultado = interpolacion_lineal(x_1=10, x_2=15, func=lambda x: 2 * x**2 - 25)
    print(f"Historial de intervalos: {resultado}")
