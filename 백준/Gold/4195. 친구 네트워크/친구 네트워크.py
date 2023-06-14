import sys
input=sys.stdin.readline

#부모 노드의 값을 얻는 함수
def getParent(parents, x):
    if parents[x] == x: return x
    #압축 과정 포함
    p = getParent(parents, parents[x])
    parents[x] = p
    return p

#두 부모 노드를 합치는 함수
def unionParent(parents,x1, x2, cnt):
    a = getParent(parents,x1)
    b = getParent(parents,x2)
    if a != b :
        parents[b] = a
        cnt[a] += cnt[b]

#루트 찾기
def findParent(x, parents):
    if parents[x] == x: return x
    return findParent(parents[x], parents)

if __name__ == "__main__":
    for _ in range(int(input())):
        parents = {}
        cnt = {}
        for test in range(int(input())):
            friend1, friend2 = input().split()

            if friend1 not in parents:
                parents[friend1] = friend1
                cnt[friend1] = 1

            if friend2 not in parents:
                parents[friend2] = friend2
                cnt[friend2] = 1

            unionParent(parents, friend1, friend2, cnt)
            print(cnt[findParent(friend1, parents)])