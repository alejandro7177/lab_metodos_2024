import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import ej_silo

# Título de la calculadora
st.title("Calculadora Científica Interactiva con Interpolación Lineal")

# Funciones permitidas en la calculadora
st.markdown("""
### Funciones permitidas:
- **Operaciones básicas**: `+`, `-`, `*`, `/`, `**` (potencia)
- **Funciones**: `sin(x)`, `cos(x)`, `tan(x)`, `log(x)`, `sqrt(x)`, `exp(x)`, etc.
- **Constantes**: `pi`, `e`
""")

# Input de expresión matemática
expresion_input = st.text_input("Introduce una expresión matemática (en función de x):")

# Rango de valores para x y error
error = st.number_input("Valor de error", value=0.00001, format='%5f')
x_min = st.number_input("Valor mínimo de x", value=-10.0)
x_max = st.number_input("Valor máximo de x", value=10.0)

# Definir la función que grafica
def funt_graf(p1_x, p2_x_fijo, p3_x, funcion):
    try:
        # Evaluar los valores de y para p1 y p3
        p1_y = funcion(p1_x)
        p3_y = funcion(p3_x)
        p2_y_fijo = funcion(p2_x_fijo)

        # Crear un rango de valores x para graficar la función completa
        x_vals = np.linspace(min(p1_x, p2_x_fijo, p3_x) - 1, max(p1_x, p2_x_fijo, p3_x) + 1, 500)
        y_vals = funcion(x_vals)

        # Calcular el cruce de la línea recta entre p1_x y p2_x_fijo con y = 0
        m = (p2_y_fijo - p1_y) / (p2_x_fijo - p1_x)  # Pendiente de la línea entre p1 y p2
        x_corte = p1_x - p1_y / m  # Punto donde la recta cruza y = 0
        y_corte = 0  # Valor de y en el punto de corte con el eje x

        # Crear el gráfico
        fig, ax = plt.subplots()
        
        # Graficar la función original
        ax.plot(x_vals, y_vals, label="Función $f(x)$", color='blue')
        
        # Graficar los puntos
        ax.scatter([p1_x], [p1_y], color='red', label=f'Punto 1 ({p1_x:.4f},{p1_y:.4f})')
        ax.scatter([p2_x_fijo], [p2_y_fijo], color='blue', label=f'Punto fijo 2 ({p2_x_fijo:.4f},{p2_y_fijo:.4f})')
        ax.scatter([p3_x], [p3_y], color='green', label=f'Nuevo Punto (x_3) ({p3_x:.4f},{p3_y:.4f})')

        # Graficar la línea de interpolación entre p1_x y p2_x_fijo
        ax.plot([p1_x, p2_x_fijo], [p1_y, p2_y_fijo], color='purple', linestyle='-.', label="Interpolación lineal")
        
        # Configuración de los ejes y leyenda
        ax.set_xlabel("x")
        ax.set_ylabel("f(x)")
        ax.set_title("Gráfico de la función con Interpolación y Corte en y=0")
        ax.grid(True)
        ax.legend()

        # Mostrar el gráfico en Streamlit
        st.pyplot(fig)
        
    except Exception as e:
        st.error(f"Error al evaluar o graficar la expresión: {e}")

if expresion_input:
    # Definir la variable para la función
    x = sp.symbols('x')
    expresion = sp.sympify(expresion_input)
    funcion = sp.lambdify(x, expresion, modules=["numpy"])

    # Calcular los puntos usando interpolación lineal del archivo ej_silo
    lista_de_puntos = ej_silo.interpolacion_lineal(x_1=x_min, x_2=x_max, func=funcion, error=error)

    # Fijar el valor de p2_x y p2_y para que no cambien (p2_x_fijo será x_max)
    x_1 = x_max

    print(lista_de_puntos)
    # Verificar que la lista de puntos no esté vacía
    if len(lista_de_puntos) > 1:
        # Barra deslizante para seleccionar el tiempo t
        t = st.slider('Seleccionar tiempo t', min_value=0, max_value=len(lista_de_puntos)-2, value=0)
        print(t)
        # Actualizar el gráfico al mover el slider
        funt_graf(
            p2_x_fijo= x_1, 
            p1_x=lista_de_puntos[t], 
            p3_x=lista_de_puntos[t+1], 
            funcion=funcion
        )
    else:
        st.error("No se generaron suficientes puntos para graficar. Verifica la función o ajusta los valores.")
    