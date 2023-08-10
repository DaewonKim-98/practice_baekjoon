import sys

N = int(sys.stdin.readline().strip())

# 스택을 둔다.
stack = []
for i in range(N):
    # 들어오는 명령에 따라 스택을 연산
    command = str(sys.stdin.readline().strip())
    if 'push' in command:
        stack.append(command[5:])
    elif 'top' in command:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    elif 'empty' in command:
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif 'size' in command:
        print(len(stack))
    elif 'pop' in command:
        if len(stack) == 0:
            print(-1)
        else:
            p = stack.pop()
            print(p)
