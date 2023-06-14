def DFS(i,j):
    global area, cnt
    dif = [(0,1),(1,0), (-1,0), (0,-1)]
    
    area[i][j] = 'v'
    cnt += 1
    for di in dif:
        ni = i + di[0]
        nj = j + di[1]
        if 0 <= ni < N and 0 <= nj < N and area[ni][nj] == '1':
            DFS(ni,nj)
    

N = int(input())
area = [list(input()) for _ in range(N)]

homes = []
for i in range(N):
    for j in range(N):
        if area[i][j] == '1':
            cnt = 0
            DFS(i,j)
            homes.append(cnt)
            
print(len(homes))

for i in sorted(homes):
    print(i)