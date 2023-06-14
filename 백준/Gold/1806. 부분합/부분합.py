N, S = map(int, input().split())
nums = list(map(int, input().split()))

st = 0
end = 0
temp_sum = nums[0]

res = N
while st < N: # r
    
    if temp_sum >= S:
        temp_cnt = end - st + 1
        if temp_cnt < res:
            res = temp_cnt
        
        temp_sum -= nums[st]
        st += 1
    elif end < N-1:
        end += 1
        temp_sum += nums[end]
    else:
        break

if st == 0:
    res = 0

print(res)