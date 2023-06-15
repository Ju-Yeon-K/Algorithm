
def grouping(i, j): # i, j 로부터 인접한 모든 상추를 2 로 바꿈
    global area
    area[i][j] = 2
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    for direction in directions:
        next_i = i + direction[0]
        next_j = j + direction[1]
        if 0 <= next_i < N and 0 <= next_j < M and area[next_i][next_j] == 1:
            grouping(next_i, next_j)



for tc in range(int(input())):
    M, N, K = map(int, input().split())
    area = [[0 for _ in range(M)]for _ in range(N)]
    for _ in range(K):
        X, Y = map(int, input().split())
        area[Y][X] = 1
    
    cnt = 0
    for i in range(N):
        for j in range(M):
            if area[i][j] == 1:
                grouping(i, j)
                cnt += 1
    
    print(cnt)