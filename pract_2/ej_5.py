import math

# Área de una piscina rectangular (valores reales)
ancho_real = math.sqrt(2)
largo_real = math.sqrt(8)

area_real = ancho_real * largo_real
print(f'El área real de la piscina es: {area_real:.15f} m^2')

# Área de una piscina con los resultados aproximados de la calculadora
ancho_aprox = 1.41
largo_aprox = 2.83

area_aprox = ancho_aprox * largo_aprox
print(f'El área aproximada de la piscina es: {area_aprox:.2f} m^2')

# Error relativo
error_relativo = abs(area_aprox - area_real) / area_real
print(f'El error relativo es: {error_relativo:.15f}')

# El valor aproximado del área (3.99 m²) no es el real debido a los errores de redondeo en las raíces
# La forma más exacta de calcular el área es utilizando los valores exactos de las raíces, sin redondearlas.
