import streamlit as st
import numpy as np
from gauss import Gauss, Format
from trapecio import Trapecios

st.title("Laboratorio Métodos Numéricos")
tab1, tab2 = st.tabs(["Método de Eliminación de Gauss", "Métodos de los Trapecio"])

with tab1:
    st.header("Método de Eliminación de Gauss")

    rows, cols = st.columns(2)

    with rows:
        num_rows = st.number_input("Filas", format="%d", min_value=0)
    with cols:
        num_cols = st.number_input("Columnas", format="%d", min_value=0)

    if num_rows+1 == num_cols:
        st.subheader("Ingresa los valores de la matriz:")
        matrix = []
        for i in range(int(num_rows)):
            row = []
            cols = st.columns(int(num_cols))  # Crear columnas horizontales para cada fila
            for j, col in enumerate(cols):
                with col:
                    value = st.number_input(
                        f"({i},{j})", 
                        key=f"cell_{i}_{j}", 
                        value=0.000, 
                        format="%.3f"
                    )
                    row.append(value)
            matrix.append(row)
        
        matrix = np.array(matrix)

        formating = Format()
        gauss = Gauss()
        if st.button(label="Calcular mediante Método de Eliminacion de Gauss"):
            stagged, solution, values = gauss.main(matrix)
            print(formating.matrix_latex(matrix=stagged[0], type=()))
            
            st.latex(formating.matrix_latex(matrix=matrix,type="()"))
            for i, (step, value) in enumerate(zip(stagged, values)):
                st.latex(value)  # Mostrar operación
                st.latex(formating.matrix_latex(matrix=step,type="()"))  # Mostrar matriz resultante
                
            st.title("Sistemas de Ecuaciones")
            st.latex(formating.matrix_to_equations(matrix=stagged[-1]))

            st.title("Resultados")
            st.latex(formating.matrix_latex(matrix=solution, type="{}"))
    else:
        st.warning("La matriz ingresada debe ser una matriz cuadrada extendida (n filas y n+1 columnas).")       

with tab2:
    st.header("Método de los Trapecios")

    num_cols_2 = st.number_input(label="Número de valores", format="%d", min_value=0)

    if not num_cols_2 == 0:
        matrix = []
        labels = ["X", "Y"]  # Etiquetas personalizadas para cada fila
        for i in range(2):
            row = []
            cols = st.columns(int(num_cols_2) + 1)
            with cols[0]:  
                st.text(labels[i] if i < len(labels) else f"Var {i+1}")
            for j, col in enumerate(cols[1:]):
                with col:
                    value = st.number_input(
                        f"({labels[i]},{j+1})",
                        key=f"cell_{i}_{j}_2",
                        value=0.0,
                        format="%.2f"
                    )
                    row.append(value)
            matrix.append(row)
            
        matrix = np.array(matrix)
        lista = matrix[0].tolist()
        distancias = [lista[i+1] - lista[i] for i in range(len(lista)-1)]

        if all(d == distancias[0] for d in distancias):
            if st.button(label="Calcular Método de Trapecios"):
                trapecios = Trapecios()
                result = trapecios.main(matrix)
                fig = trapecios.graf(matrix, str(result) )
                st.pyplot(fig)
                st.write(f"Resultado: {result}")
        else:
            st.warning("Los valores ingresados deben ser x distantes")

#streamlit run app.py


