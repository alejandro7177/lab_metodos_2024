# Medidas en metros
medida_1 = 1
error_1 = 0.001

medida_2 = 300000
error_2 = 300

# Error relativo
error_relativo_1 = error_1 / medida_1
error_relativo_2 = error_2 / medida_2

# Mostrar resultados con formato similar a fprintf
print(f'Error relativo para 1 metro: {error_relativo_1:.15f} ({error_relativo_1 * 100:.2f}%)')
print(f'Error relativo para 300 Km: {error_relativo_2:.15f} ({error_relativo_2 * 100:.2f}%)')

# Comparación de errores relativos
if error_relativo_1 > error_relativo_2:
    print('El error relativo para 1 metro es mayor.')
elif error_relativo_1 < error_relativo_2:
    print('El error relativo para 300 Km es mayor.')
else:
    print('Ambos errores relativos son iguales.')
