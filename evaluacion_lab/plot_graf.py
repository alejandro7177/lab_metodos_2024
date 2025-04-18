import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def plot_newtonraphson_results(f, table:pd.DataFrame, execution_time):
    x_values = table['x']
    fx_values = table['f(x)']

    x_range = np.linspace(min(x_values) -0.05, max(x_values) + 0.05, 1500)
    y_range = f(x_range)

    plt.figure(figsize=(8, 6))
    plt.plot(x_range, y_range, label='f(x)', color='r', linewidth=2)

    plt.plot(x_values, fx_values, marker='o', linestyle='-', color='b', label='Newton-Raphson Puntos')

    plt.title('Newton-Raphson Iteraciones')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid(True)
    plt.legend()

    plt.text(0.95, 0.95, f'Time: {execution_time:.5f} s', fontsize=12, color='green',verticalalignment='top', horizontalalignment='right', transform=plt.gcf().transFigure,bbox=dict(facecolor='white', alpha=0.5))

    plt.savefig("images/grafico_newton_raphson.png",format='png', dpi=300)

def plot_function(f):

    x_vals = np.linspace(-2, 2, 30)
    y_vals = f(x_vals)
    plt.figure(figsize=(8, 6))
    plt.plot(x_vals, y_vals, label='f(x)', color='blue', linewidth=2)

    plt.title('Grafico de la Función')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid(True)
    plt.legend()

    plt.savefig("images/graf_function.png",format='png', dpi=300)


if __name__ == "__main__":
    f = lambda x: x**2
    plot_function(f)
