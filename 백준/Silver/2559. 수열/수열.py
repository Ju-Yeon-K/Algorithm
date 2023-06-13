N, K = map(int, input().split())
nums = list(map(int, input().split()))

if N == K:
    res = sum(nums)
else:
    temp = 0
    for i in range(K):
        temp += nums[i]
    res = -10000000
    for i in range(N-K):
        if res < temp:
            res = temp
        temp += nums[i+K] - nums[i]
    if res < temp:
            res = temp
print(res)