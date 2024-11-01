import pandas as pd
from time import time
from validacition_inputs import validar_funcion, validar_error, validar_x
from plot_graf import plot_newtonraphson_results, plot_function
from conditionFourier import fourier

def NewtonRaphson():
    f, df = validar_funcion()

    plot_function(f)

    x0 = validar_x(i=0)
    x1 = validar_x(i=1)

    #vefifica la condicion de fourier
    fourier_result = fourier(f, x1=x1, x0=x0)

    value = next((clave for clave, valor in fourier_result.items() if valor), None)

    if value:
        print('Se cumple la condicion de fourier correctamente!!')
        print(f'Se inicializa la interacion con {value}')
        error = validar_error()
        x0 = value
        x1 = None

        count = 0
        table = pd.DataFrame(columns=["x","f(x)","e"])
        row = [x0,f(x0),""]
        table.loc[len(table)] = row
        start = time()
        while True:
            x1 = x0 - f(x0) / df(x0)
            error_actual = abs(x1 - x0)
            row = [x1,f(x1),error_actual]
            table.loc[len(table)] = row
            if error_actual < error:
                break
            x0 = x1
            count += 1
        end = time()
        print(table)
        print(f"tiempo de ejecucion: {end-start} seg")

        plot_newtonraphson_results(
            f=f,
            table=table,
            execution_time=end-start
        )
        table.to_csv('data/table_newton_raphson.csv')
    else:
        print("x0 y x1 no cumple con la condicion de fourier")

if __name__ == '__main__':
    NewtonRaphson()

