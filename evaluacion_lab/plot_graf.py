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

    plt.plot(x_values, fx_values, marker='o', linestyle='-', color='b', label='Newton-Raphson Points')

    plt.title('Newton-Raphson Iterations with f(x)')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid(True)
    plt.legend()

    plt.text(0.95, 0.95, f'Time: {execution_time:.5f} s', fontsize=12, color='green',verticalalignment='top', horizontalalignment='right', transform=plt.gcf().transFigure,bbox=dict(facecolor='white', alpha=0.5))

    plt.savefig("grafico.png",format='png', dpi=300)