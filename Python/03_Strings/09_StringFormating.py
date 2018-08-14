def print_formatted(number):
    w = len(format(number, 'b'))

    for i in range(1, number+1):
        print('{number:{width}d} {number:{width}o} {number:{width}X} {number:{width}b}'.format(number=i, width=w))

if __name__=='__main__':
    n = int(input())
    print_formatted(n)
