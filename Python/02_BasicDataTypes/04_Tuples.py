def main(integer_list):
    _hash = hash(tuple(integer_list))
    print(_hash)

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())

    main(integer_list)
