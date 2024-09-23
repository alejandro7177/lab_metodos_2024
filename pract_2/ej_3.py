import math

# Coeficientes
a = 1
b = 1e8  # 10^8

# Caso 1: c = 1
c1 = 1

# Discriminante
discriminante1 = b**2 - 4 * a * c1

# Vemos si el discriminante es positivo
if discriminante1 >= 0:
    # Incógnitas
    x1_1 = (-b + math.sqrt(discriminante1)) / (2 * a)
    x2_1 = (-b - math.sqrt(discriminante1)) / (2 * a)
    print(f'Soluciones para c = 1: x1 = {x1_1:.5e}, x2 = {x2_1:.5e}')
else:
    print('No hay soluciones reales para c = 1.')

# Caso 2: c = 10^8
c2 = 1e8

# Discriminante
discriminante2 = b**2 - 4 * a * c2

# Vemos si el discriminante es positivo
if discriminante2 >= 0:
    # Incógnitas
    x1_2 = (-b + math.sqrt(discriminante2)) / (2 * a)
    x2_2 = (-b - math.sqrt(discriminante2)) / (2 * a)
    print(f'Soluciones para c = 10^8: x1 = {x1_2:.6e}, x2 = {x2_2:.6e}')
else:
    print('No hay soluciones reales para c = 10^8.')

# c = 1: La medida tenía errores debido a la complejidad del cálculo del discriminante y su pequeña magnitud
# c = 10^8: Los cálculos son más consistentes, mostrando que cuando c es grande, los resultados son más esperados.
