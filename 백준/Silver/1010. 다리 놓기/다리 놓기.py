
for tc in range(int(input())):
    N, M = map(int, input().split())

    if N > M:
        M, N = N, M
        
    res = 1
    for i in range(M, M-N, -1):
        res *= i

    for i in range(1, N+1):
        res //= i

    print(res)