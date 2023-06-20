def solution(queue1, queue2):
    q = queue1 + queue2
    N = len(queue1) 
    dif = sum(queue2)-sum(queue1)
    res, idx1, idx2 = 0, 0, N
    for i in range(300000):
    # while dif != 0:
        if dif == 0:
            return res
        if idx1 == idx2:
            return -1

        if dif > 0:
            dif -= 2*q[idx2]
            idx2 = (idx2 + 1 ) % (2*N)
        elif dif < 0:
            dif += 2*q[idx1]
            idx1 = (idx1 + 1 ) % (2*N)
        res += 1
    else:
        return -1
    return res