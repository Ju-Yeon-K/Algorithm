def fac_list(N,K):
    res = [[0]*(N+1) for _ in range(K+1)]
    for j in range(N+1):
        res[0][j] = 1
    for i in range(K+1):
        res[i][i] = 1

    for i in range(1, K+1):
        for j in range(i+1, N+1):
            res[i][j] = res[i][j-1] + res[i-1][j-1]
    return res

N, K = map(int,input().split())
res_list = fac_list(N,K)
res = res_list[K][N] % 10007
print(res)