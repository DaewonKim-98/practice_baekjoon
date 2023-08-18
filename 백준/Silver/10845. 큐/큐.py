import sys
from collections import deque
input = sys.stdin.readline

N = int(input().strip())

queue = []
for i in range(N):
    commend = list(map(str, input().split()))

    if commend[0] == 'push':
        queue.append(commend[1])
    elif commend[0] == 'pop':
        if queue:
            print(queue.pop(0))
        else:
            print(-1)
    elif commend[0] == 'size':
        print(len(queue))
    elif commend[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif commend[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif commend[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)