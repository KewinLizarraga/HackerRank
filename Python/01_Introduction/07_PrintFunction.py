"""
Read an integer N.
Without using any string methods, try to print the following:
123...N
Note that "..." represents the values in between.
"""

def number(n):
    for i in range(n):
        print(i+1,end="")

if __name__ == '__main__':
    n = int(input())

    number(n)
