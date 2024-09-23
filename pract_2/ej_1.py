import math

def ej_1():
    sin_redondeo = str(math.pi/ math.exp(1))
    redondeo = str(round(math.pi,6)/round(math.exp(1),6))

    print(f"e/pi real = {sin_redondeo}\n")
    print(f"e/pi red = {redondeo}")

    count = 0
    for i, j in zip(sin_redondeo, redondeo):
        if i == j:
            if i == '0' or i == '.':
                continue
            count += 1
        else:
            break
    dif = abs(float(redondeo) - float(sin_redondeo))
    print(f'Diferencia entre el exacto y el redondeado {dif}')
    print(f'cantidad de digitos significativos: {count}')

if __name__ == '__main__':
    ej_1()