import sys
input = sys.stdin.readline

def counting(N):
    arr[1] = 0
    for i in range(2, N + 1):
        # 최솟값은 1을 뺀 것이거나 3 또는 2를 나눈 것 중에서 최소
        arr[i] = arr[i - 1] + 1
        if i % 2 == 0:
            arr[i] = min(arr[i- 1] + 1, arr[i // 2] + 1)  
        if i % 3 == 0:
            arr[i] = min(arr[i - 1] + 1, arr[i // 3] + 1)               
            
    return arr[N]
N = int(input().strip())
arr = [0] * (N + 1)


print(counting(N))

