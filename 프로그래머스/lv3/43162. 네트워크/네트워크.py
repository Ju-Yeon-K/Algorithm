def FindSet(rep, x):
    while x != rep[x]:
        x = rep[x]
    return x

def Union(rep, x, y):
    a = FindSet(rep, x)
    b = FindSet(rep, y)
    rep[a] = b

def solution(n, computers):
    rep = [i for i in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            if computers[i][j] == 1:
                Union(rep, i, j)
    fin_set = set()
    for i in rep:
        fin_set.add(FindSet(rep, i))

    return len(fin_set)