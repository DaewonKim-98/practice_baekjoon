from collections import deque
import sys

input = sys.stdin.readline
deck = deque([])

N = int(input())
for i in range(N):
    commend = deque(list(map(int, input().split())))
    if commend[0] == 1:
        deck.appendleft(commend[1])
    elif commend[0] == 2:
        deck.append(commend[1])
    elif commend[0] == 3:
        if deck:
            print(deck.popleft())
        else:
            print(-1)
    elif commend[0] == 4:
        if deck:
            print(deck.pop())
        else:
            print(-1)
    elif commend[0] == 5:
        print(len(deck))
    elif commend[0] == 6:
        if deck:
            print(0)
        else:
            print(1)
    elif commend[0] == 7:
        if deck:
            print(deck[0])
        else:
            print(-1)
    elif commend[0] == 8:
        if deck:
            print(deck[-1])
        else:
            print(-1)