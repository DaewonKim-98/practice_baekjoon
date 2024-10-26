N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

cnt = 0
# 가장 먼 것들은 왕복하지말고 그냥
cnt += max(abs(arr[0]), abs(arr[-1]))
i = 0
if abs(arr[0]) > abs(arr[-1]):
    while i < M and arr and arr[0] < 0:
        arr.pop(0)
        i += 1
else:
    while i < M and arr and arr[-1] > 0:
        arr.pop()
        i += 1

# 나머지는 모두 왕복
N = len(arr)
i = 0
while i < N and arr[i] < 0:
    cnt += -arr[i] * 2
    i += M
i = N - 1
while 0 <= i and arr[i] > 0:
    cnt += arr[i] * 2
    i -= M
    
print(cnt)