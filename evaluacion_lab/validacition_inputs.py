import sympy as sp
from sympy.core.sympify import SympifyError

def validar_funcion():
    x = sp.symbols('x')
    while True:
        f_input = input("Digite la función (con variable x): ")

        if f_input == "!exit" or "exit":
            exit

        try:
            f_simb = sp.sympify(f_input)
            df_simb = sp.diff(f_simb, x)

            f = sp.lambdify(x, f_simb)
            df = sp.lambdify(x, df_simb)

            if not f_simb.has(x):
                print("Error: La función debe depender de la variable 'x'.")
                print("Digite una función válida (ej. 'sqrt(x) + x**2')\n")
                continue
            return f, df
        except SympifyError:
            print("Error: El input no es una función válida. Inténtalo de nuevo.")
            print("Digite una función válida (ej. 'sqrt(x) + x**2')\n")

def validar_error()->float:
    while True:
        e_input = input("\nIngrese el error (default 0.001):")
        if e_input == "":
            return 0.001
        try:
            error = float(e_input)
            if error > 0.001:
                print("El error debe ser menor a 0.001")
                continue
            return error
        except ValueError:
            print("Error no válido, por favor ingrese un número.")

def validar_x(i:int)->float:
    while True:
        x_input = input(f"ingrese el x_{i}:")
        try:
            x = float(x_input)
            return x
        except ValueError:
            print(f"x{i} no válido, por favor ingrese un número.")