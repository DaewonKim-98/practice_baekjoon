import sys
from collections import deque
input = sys.stdin.readline

N = int(input().strip())
# 사람들을 리스트화
arr = deque(range(1, N + 1))
# 처음 t는 1
t = 1

# 배열에 한 명이 남을 때까지 반복
while len(arr) > 1:
    # t 단계일 경우 t**3 전까지 돌린다.
    # 그런데 이러면 시간이 너무 잡아먹히므로 t ** 3이 len(arr)보다 크다면
    # 나머지만큼만 돌린다.
    if t ** 3 > len(arr):
        k = (t ** 3) % len(arr)
    else:
        k = t ** 3
    for i in range(k):
        arr.append(arr.popleft())
    # 돌리는 것이 끝났으면 백준이가 앞에 서 있는 사람은 가장 마지막에 돌아간 사람
    # 가장 뒤의 사람일 것이므로
    arr.pop()
    # 단계 추가
    t += 1

print(arr[0])