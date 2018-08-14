def design(N, M):

    for i in range(0, N//2):
        print(('.|.'*i+'.|.'+'.|.'*i).center(M,'-'))

    print(('WELCOME').center(M,'-'))

    for i in range(N//2-1, -1, -1):
        print(('.|.'*i+'.|.'+'.|.'*i).center(M,'-'))

if __name__=='__main__':
    N, M = map(int, input().split())

    design(N, M)
