import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
# 합의 리스트
lst = [0] * N
lst[0] = arr[0]
for i in range(1, N):
    lst[i] = lst[i - 1] + arr[i]

for _ in range(M):
    i, j = map(int, input().split())
    if i == 1:
        print(lst[j - 1])
    else:
        print(lst[j - 1] - lst[i - 2])
