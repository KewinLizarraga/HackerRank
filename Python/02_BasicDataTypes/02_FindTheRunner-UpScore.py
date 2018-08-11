"""
Find the score of the second maximum.
"""

def find_second_max(arg):
    arg.sort()
    second_max =-2

    for i in range(len(arg)):
        if arg[second_max] == arg[-1]:
            second_max -= 1

    return second_max

if __name__=="__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    second = find_second_max(arr)
    print(second)
