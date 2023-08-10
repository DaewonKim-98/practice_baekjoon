import sys

K = int(sys.stdin.readline().strip())

stack = []
for i in range(K):
    N = int(sys.stdin.readline().strip())
    # 만약 N이 0일 때
    if N == 0:
        # 만약 stack에 원소가 있을 때 지운다.
        if len(stack) != 0:
            stack.pop()
        # 만약 stack에 원소가 없으면 지나간다.
        else:
            pass
    # N이 0이 아닐 때
    else:
        stack.append(N)

print(sum(stack))