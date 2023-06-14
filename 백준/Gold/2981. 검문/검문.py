N = int(input())
numbers = [int(input()) for _ in range(N)]
first = min(numbers)
numbers = [i - first for i in numbers]
numbers.remove(0)
new_min = min(numbers) 
temp_list = []
for i in range(2,new_min+1):
    for a in numbers:
        if a % i:
            break
    else:
        temp_list.append(i)

print(*sorted(temp_list))