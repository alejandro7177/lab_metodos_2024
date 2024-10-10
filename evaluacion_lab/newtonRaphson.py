import pandas as pd
from time import time
from validacition_inputs import validar_funcion, validar_error, validar_x0
from plot_graf import plot_newtonraphson_results

def NewtonRaphson():
    f, df = validar_funcion()
    error = validar_error()
    x0 = validar_x0()
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
    table.to_csv('table.csv')

NewtonRaphson()

