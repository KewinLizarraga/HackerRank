"""
Leer dos numeros e imprimir tres lineas donde:
1. La primera linea contiene la suma de los dos numeros
2. La segunda linea contiene la diferencia de los dos numeros (primero-segundo)
3. La tercera linea contiene el producto de los dos numeros
"""
def sum(a, b):
    return a+b

def dif(a, b):
    return a-b

def prod(a, b):
    return a*b


if __name__ == '__main__':
    a = int(input())
    b = int(input())

    print(sum(a, b))
    print(difference(a, b))
    print(product(a, b))
