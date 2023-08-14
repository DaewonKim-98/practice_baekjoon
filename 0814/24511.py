from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
A = deque(list(map(int, input().split())))
B = deque(list(map(int, input().split())))
M = int(input())
C = deque(list(map(int, input().split())))

# 큐스택
queuestack = B
# C의 원소를 차례대로 삽입해야 하므로
for c in C:
    p = c
    for i in range(N):
        # A의 원소가 1일 때는 p와 큐스택 안의 값이 바뀌지 않으므로 0일 때만 본다.
        if A[i] == 0:
            # 원소가 0일 때는 p와 남아있는 것들이 서로 바뀐다.
            queuestack[i], p = p, queuestack[i]
    print(p, end=' ')