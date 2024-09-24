import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import ej_silo

# Título de la calculadora
st.title("Calculadora Científica Interactiva con Puntos Móviles en Tiempo")

# Funciones permitidas en la calculadora
st.markdown("""
### Funciones permitidas:
- **Operaciones básicas**: `+`, `-`, `*`, `/`, `**` (potencia)
- **Funciones**: `sin(x)`, `cos(x)`, `tan(x)`, `log(x)`, `sqrt(x)`, `exp(x)`, etc.
- **Constantes**: `pi`, `e`
""")

# Input de expresión matemática
expresion_input = st.text_input("Introduce una expresión matemática (en función de x):")

# Rango de valores para x
error = st.number_input("Valor de error", value=0.001, format='%6f')
x_min = st.number_input("Valor mínimo de x", value=-10.0)
x_max = st.number_input("Valor máximo de x", value=10.0)


# Definir la función que grafica
def funt_graf(t, lista_de_puntos):
    try:
        # Definir la variable x
        x = sp.symbols('x')
        
        expresion = sp.sympify(expresion_input)
        
        st.write("### Expresión en formato LaTeX:")
        st.latex(sp.latex(expresion))
        
        funcion = sp.lambdify(x, expresion, modules=["numpy"])

        x_vals = np.linspace(x_min, x_max, 500)
        
        y_vals = funcion(x_vals)
        
        p1_x, p2_x = lista_de_puntos[t]
        p1_y = funcion(p1_x)
        p2_y = funcion(p2_x)

        # Crear el gráfico
        fig, ax = plt.subplots()
        ax.plot(x_vals, y_vals, label=f"$f(x) = {sp.latex(expresion)}$")
        ax.scatter([p1_x], [p1_y], color='red', zorder=5, label=f'Punto 1 coords: ({p1_x:.4f},{p1_y:.4f})')
        ax.scatter([p2_x], [p2_y], color='red', zorder=5, label=f'Punto 2 coords: ({p2_x:.4f},{p2_y:.4f})')
        ax.set_xlabel("x")
        ax.set_ylabel("f(x)")
        ax.set_title("Gráfico de la función con puntos móviles")
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

    print(lista_de_puntos)

    # Barra deslizante para seleccionar el tiempo t
    t = st.slider('Seleccionar tiempo t', min_value=0, max_value=len(lista_de_puntos)-1, value=0)

    funt_graf(t, lista_de_puntos)
