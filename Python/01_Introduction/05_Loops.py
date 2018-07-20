"""
Read an integer N. For all non-negative integers i<N, print i².
"""

def loops(n):
    for i in range(n):
        print(i**2)

if __name__ == '__main__':
    n = int(input())

    loops(n)
