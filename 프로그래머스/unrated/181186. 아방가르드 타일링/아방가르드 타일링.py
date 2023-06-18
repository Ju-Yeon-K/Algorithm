def solution(n):
    arr = [1, 1, 3, 10, 23, 62] + [0 for _ in range(n-4)]
    if n > 5:
        for i in range(6, n+1):
            arr[i] = arr[i-1] + 2*arr[i-2] + 6*arr[i-3] + arr[i-4] - arr[i-6] 
        arr[i] = arr[i] % 1000000007

    return arr[n]