import numpy as np
from typing import Literal

class Gauss():
    def main(self, matrix:np.ndarray)->tuple[list[np.ndarray], np.ndarray, list]:
        matrix_r = matrix.copy().astype(float)  # Copia la matriz para evitar modificaciones externas
        operations = []  # Lista para registrar las operaciones elementales realizadas
        steps = []  # Lista para almacenar las matrices después de cada paso de eliminación

        # Eliminación hacia adelante
        for i in range(matrix_r.shape[0] - 1):  # Recorre las filas principales
            for j in range(i + 1, matrix_r.shape[0]):  # Recorre las filas inferiores
                if matrix_r[i, i] == 0:
                    continue  # Evita divisiones por cero
                factor = matrix_r[j, i] / matrix_r[i, i]  # Calcula el factor de eliminación
                operation = f"F_{{{j+1}}} \\to F_{{{j+1}}} - {factor:.1f}F_{{{i+1}}}"
                operations.append(operation)  # Registra la operación
                matrix_r[j] = matrix_r[j] - factor * matrix_r[i]  # Realiza la eliminación
                steps.append(matrix_r.copy())  # Guarda el estado actual de la matriz

        n = matrix_r.shape[0]  # Número de filas o incógnitas
        solution = np.zeros(n)  # Vector para almacenar las soluciones

        # Sustitución hacia atrás
        for i in range(n-1, -1, -1):  # Empieza desde la última fila hacia la primera
            solution[i] = (matrix_r[i, -1] - np.dot(matrix_r[i, i+1:n], solution[i+1:n])) / matrix_r[i, i]

        return steps, solution.reshape(-1, 1), operations  # Devuelve los pasos, la solución y las operaciones

class Format():

    def format_value(self, value):
        return str(int(value)) if value == int(value) else f"{value:.2f}"

    def matrix_latex(self, matrix, type: Literal["()","[]", "{}"]):
        """
        Convierte un numpy array en formato LaTeX utilizando \begin{pmatrix} ... \end{pmatrix}.
        """
        rows = [" & ".join(map(self.format_value, row)) for row in matrix]
        if type == "[]":
            return "\\begin{Bmatrix}\n" + " \\\\\n".join(rows) + "\n\\end{Bmatrix}"
        elif type == "{}":
            return "\\begin{bmatrix}\n" + " \\\\\n".join(rows) + "\n\\end{bmatrix}"
        
        return "\\begin{pmatrix}\n" + " \\\\\n".join(rows) + "\n\\end{pmatrix}"

    def matrix_to_equations(self, matrix:np.ndarray, variables=None)->str:
        rows, cols = matrix.shape
        if variables is None:
            variables = [f"x_{i+1}" for i in range(cols - 1)]
        elif len(variables) != cols - 1:
            raise ValueError("El número de variables debe coincidir con las columnas de la matriz menos una.")
        
        equations = []
        for row in matrix:
            equation = " + ".join([f"{self.format_value(coef)}{var}" for coef, var in zip(row[:-1], variables) if coef != 0])
            equation += f" = {self.format_value(row[-1])}"
            equations.append(equation)
        
        # Combinar ecuaciones en formato LaTeX con \begin{cases}
        latex_system = "\\begin{cases}\n" + " \\\\\n".join(equations) + "\n\\end{cases}"
        return latex_system

if __name__ == "__main__":
    matrix = np.array([
    [2,6,1,7],
    [1,2,-1,-1],
    [5,7,-4,9]
    ])

    stagged, solution, v = Gauss.main(matrix=matrix)
    print(stagged)
    print(stagged[-1].shape[0])