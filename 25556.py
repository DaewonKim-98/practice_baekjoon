N = int(input())
arr = list(map(int, input().split()))

stacks = [[] for _ in range(4)]

for i in range(N):
    canAppend = False
    for stack in stacks:
        # 스택이 비어있으면 걍 넣기
        if not stack:
            stack.append(arr[i])
            canAppend = True
            break
        # 스택이 비어있지 않으면 자기보다 작은게 있을때 넣기
        if stack[-1] < arr[i]:
            stack.append(arr[i])
            canAppend = True
            break
    # 모든 스택에 넣을 수 없다면
    if canAppend == False:
        print('NO')
        exit()

# exit이 되지 않았다면
print('YES')