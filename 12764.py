import sys
import heapq

input = sys.stdin.readline

N = int(input().strip())
arr = [list(map(int, input().strip().split())) for _ in range(N)]
arr.sort()

computers = []
empty = []

heapq.heappush(computers, [arr[0][1], 0])
useComputers = [1]

for i in range(1, N):
    start, end = arr[i]

    # 종료 시간이 가장 빠른 컴퓨터를 확인
    while computers and computers[0][0] < start:
        # 빈 자리에 컴퓨터를 추가
        heapq.heappush(empty, heapq.heappop(computers)[1])

    if empty:
        # 빈 자리가 있으면 자리 넣기
        minNumber = heapq.heappop(empty)
        heapq.heappush(computers, [end, minNumber])
        useComputers[minNumber] += 1
    else:
        # 빈 자리가 없으면 새 컴퓨터를 추가
        heapq.heappush(computers, [end, len(useComputers)])
        useComputers.append(1)

print(len(useComputers))
for use in useComputers:
    print(use, end=' ')
