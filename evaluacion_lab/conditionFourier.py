import sympy as sp

def fourier(f, x0, x1) -> dict[float:bool]:
    """
    Evalúa las condiciones de Fourier en los puntos `x0` y `x1` para una función `f`.
    
    Args:
        f (callable): Función a evaluar.
        x0 (float): Punto inicial para evaluar.
        x1 (float): Punto final para evaluar.
        
    Returns:
        dict[float:bool]: Un diccionario que indica si cada punto cumple con la condición.
    """
    # Define la variable simbólica `x` para las operaciones de derivada
    x = sp.symbols('x')
    
    # Convierte la función `f` a su representación simbólica para derivación
    f_simb = f(x)
    
    # Inicializa el diccionario `result` para almacenar los resultados de Fourier
    # para cada punto `x0` y `x1`, inicialmente como `False`.
    result = {x0: False, x1: False}
    
    # Verifica si el producto f(x0) * f(x1) > 0.
    # Si es así, significa que ambos puntos tienen el mismo signo y el método Newton-Raphson puede no converger.
    if f(x0) * f(x1) > 0:
        result  # (Esta línea no tiene ningún efecto en el código actual y puede ser eliminada)
    
    # Calcula la primera derivada de la función `f_simb` con respecto a `x`.
    primera_derivada = sp.diff(f_simb, x)
    
    # Calcula la segunda derivada de `f_simb` (la derivada de `primera_derivada`) con respecto a `x`.
    segunda_derivada = sp.diff(primera_derivada, x)
    
    # Convierte la segunda derivada a una función evaluable (lambda function)
    # para poder evaluar la segunda derivada en valores numéricos como `x0` y `x1`.
    ddf = sp.lambdify(x, segunda_derivada)
    
    # Comprueba la condición de Fourier en el punto `x0`.
    # Si f(x0) * ddf(x0) > 0, significa que la función y la segunda derivada
    # en `x0` tienen el mismo signo, y el punto cumple con la condición.
    if f(x0) * ddf(x0) > 0:
        result[x0] = True  # Marca `x0` como que cumple la condición.
    
    # Comprueba la misma condición en el punto `x1`.
    if f(x1) * ddf(x1) > 0:
        result[x1] = True  # Marca `x1` como que cumple la condición.
    
    # Devuelve el diccionario `result` con los resultados para `x0` y `x1`.
    return result
