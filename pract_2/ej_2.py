# Medidas reales y obtenidas
medida_folio_real = 29.6
medida_folio_obtenida = 30.0

medida_pupitre_real = 65.0
medida_pupitre_obtenida = 65.4

# Error absoluto
error_folio = abs(medida_folio_obtenida - medida_folio_real)
error_pupitre = abs(medida_pupitre_obtenida - medida_pupitre_real)

# Error relativo
error_relativo_folio = error_folio / medida_folio_real
error_relativo_pupitre = error_pupitre / medida_pupitre_real

# Mostrar resultados con precisión de 15 decimales
print(f'Error relativo del folio: {error_relativo_folio:.15f}')
print(f'Error relativo del pupitre: {error_relativo_pupitre:.15f}')

# Comparación de precisión
if error_relativo_folio < error_relativo_pupitre:
    print('La medida del folio es más precisa.')
elif error_relativo_folio > error_relativo_pupitre:
    print('La medida del pupitre es más precisa.')
else:
    print('Ambas mediciones tienen la misma precisión.')
