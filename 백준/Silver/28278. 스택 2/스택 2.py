import sys
input = sys.stdin.readline

N = int(input().strip())

stack = []
for i in range(N):
    commend = list(map(int, input().split()))
    
    if commend[0] == 1:
        stack.append(commend[1])
    elif commend[0] == 2:
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif commend[0] == 3:
        print(len(stack))
    elif commend[0] == 4:
        if stack:
            print(0)
        else:
            print(1)
    else:
        if stack:
            print(stack[-1])
        else:
            print(-1)