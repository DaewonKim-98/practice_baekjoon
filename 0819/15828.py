import sys
from collections import deque
input = sys.stdin.readline

N = int(input().strip())
imformation = deque([])
router = deque([])
while True:
    i = int(input().strip())
    if i == -1:
        break
    imformation.append(i)


# while문을 돌리면서 0일 때는 빼내고 아닐 때는 넣는다.
while len(imformation) > 0:
    if imformation[0] != 0:
        # router의 길이의 최대는 N 이므로 N보다 router가 작을 때만 넣는다.
        if len(router) < N:
            router.append(imformation.popleft())
        else:
            imformation.popleft()
    else:
        imformation.popleft()
        router.popleft()

if len(router) > 0:
    print(*router)
else:
    print('empty')