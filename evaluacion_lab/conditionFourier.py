import sympy as sp

def fourier(f, x0, x1)->dict[float:bool]:
    x = sp.symbols('x')
    f_simb = f(x)
    result = {x0:False, x1:False}

    if f(x0)*f(x1) > 0:
        result

    primera_derivada = sp.diff(f_simb, x)
    segunda_derivada = sp.diff(primera_derivada, x)

    ddf = sp.lambdify(x, segunda_derivada)

    if f(x0)*ddf(x0)>0:
        result[x0] = True
    if f(x1)*ddf(x1)>0:
        result[x1] = True

    return result

if __name__=='__main__':
    x0 = input("ingrese el valor para verificar la funcion x0: ")
    x1 = input("ingrese el valor para verificar la funcion x1: ")
    f = lambda x:6*x**2+3*x-2

    result = fourier(f,x0,x1)

    print("x0", "cumple" if result[0] else "no cumple")
    print("x1", "cumple" if result[1] else "no cumple")