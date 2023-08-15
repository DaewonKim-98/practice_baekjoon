import sys
from collections import deque

N = int(sys.stdin.readline())

arr = [i for i in range(1, N+1)]
deq = deque(arr)

# deq가 0이 될 때까지 하나를 버리고 다음 것을 가장 오른 쪽으로 옮긴다.
while len(deq) > 1 :
    deq.popleft()
    top = deq.popleft()
    deq.append(top)

print(deq[0])