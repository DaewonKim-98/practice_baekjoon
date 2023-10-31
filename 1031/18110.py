import math
from collections import deque

N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort()
arr = deque(arr)
if N == 0:
    print(0)
else:
    # 위 아래 15%씩 제외
    if N * (15 / 100) + 0.5 >= math.ceil(N * (15 / 100)):
        exclude = math.ceil(N * (15 / 100))
    else:
        exclude = math.floor(N * (15 / 100))
    for i in range(exclude):
        arr.popleft()
        arr.pop()

    # 절사평균
    if sum(arr) / (N - 2 * exclude) + 0.5 >= math.ceil(sum(arr) / (N - 2 * exclude)):
        average = math.ceil(sum(arr) / (N - 2 * exclude))
    else:
        average = math.floor(sum(arr) / (N - 2 * exclude))

    print(average)