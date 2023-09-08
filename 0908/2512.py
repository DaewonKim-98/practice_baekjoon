import sys
input = sys.stdin.readline

N = int(input().strip())
arr = list(map(int, input().split()))
M = int(input().strip())
arr.sort()

# 이진탐색을 통해 상한액 찾기
start, end = 0, arr[-1]
result = 0

while start <= end:
    middle = (start + end) // 2
    s = 0
    for i in range(N):
        s += min(arr[i], middle)
    
    if s <= M:
        result = middle
        start = middle + 1
    else:
        end = middle - 1

print(result)