def is_1_surround(i, j):
    global arr
    dif = [(0,1), (1,0), (0, -1), (-1,0)]
    arr [i][j] = 2

    for case in dif:
        temp_i = i+ case[0]
        temp_j = j+ case[1]
        if 0 <= temp_i < N and 0 <= temp_j < M and arr[temp_i][temp_j] == 1:
            is_1_surround(temp_i, temp_j)



T = int(input())
for tc in range(1, T+1):
    M, N, K = map(int,input().split())
    arr = [[0]*M for _ in range(N)]
    for _ in range(K):
        x, y = map(int,input().split())
        arr[y][x] = 1
    
    res = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                is_1_surround(i,j)
                res += 1
    print(res)
