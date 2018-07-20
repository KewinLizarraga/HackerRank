"""
Read two numbers and print three lines where:
1. The first line contains the sum of the two numbres.
2. The second line contains the difference of the two numbers(first-second)
3. The third line contains the product of the two numbers.
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
