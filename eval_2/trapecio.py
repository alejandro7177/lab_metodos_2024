import numpy as np
import matplotlib.pyplot as plt


class Trapecios():
    def main(self, vector:np.ndarray):
        lista = vector[0]
        distancias = [lista[i+1] - lista[i] for i in range(len(lista)-1)]
        h = distancias[0]
        E = vector[1,0]+ vector[1,-1]
        P = np.array([
            num if i%2 == 0 else 0 for i, num in enumerate(vector[1][:-1], 1)
        ]).sum()
        I = np.array([
            0 if i%2 == 0 else num for i, num in enumerate(vector[1][1:-1], 0)
        ]).sum()

        print("h:",h)
        print("E:",E)
        print("P:",P)
        print("I:",I)
        return (h/2)*(E+2*P+2*I)

    def graf(self, matrix: np.ndarray, area_label:str, dim: tuple[int, int] = (8, 6)) -> plt.Figure:
        """
        Genera un gráfico con el área bajo los puntos dividida en segmentos.

        Args:
            matrix (np.ndarray): Matriz 2xN con coordenadas X en la primera fila y Y en la segunda.
            dim (tuple[int, int]): Dimensiones del gráfico (ancho, alto) en pulgadas.

        Returns:
            plt.Figure: Objeto Matplotlib Figure.
        """
        x = matrix[0].tolist()  # Coordenadas X
        y = matrix[1].tolist()  # Coordenadas Y

        # Crear el gráfico
        fig, ax = plt.subplots(figsize=(dim[0], dim[1]))

        # Graficar puntos y líneas
        ax.plot(x, y, marker='o', label="Puntos y líneas")

        # Dividir y sombrear el área bajo cada segmento
        for i in range(len(x) - 1):
            ax.fill_between(
                x[i:i+2],  # Puntos X del segmento
                y[i:i+2],  # Puntos Y del segmento
                alpha=0.5,
                color="skyblue",  # Cambiar colores para cada segmento
                label = f"Area ≈ {area_label}" if i == 0 else ""
            )

        # Etiquetas y leyenda
        ax.set_title("Área bajo los trapecios", fontsize=14)
        ax.set_xlabel("X", fontsize=12)
        ax.set_ylabel("Y", fontsize=12)
        ax.legend()

        return fig



if __name__ == "__main__":
    trapecio = Trapecios()
    vector = np.array([
        [0.5, 5.5, 10.5, 15.5, 20.5, 25.5],
        [0.05, 6.05, 22.05, 48.05, 84.05, 130.05]
    ])
    result = trapecio.main(vector)
    print(result)