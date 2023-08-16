from collections import deque
import sys
input = sys.stdin.readline

arr = deque(list(input().strip()))
# 커서에 따라서 arr에서 커서의 오른쪽 부분을 narr로 옮긴다.
narr = deque(list())
N = int(input().strip())
for commend in range(N):
    commend = deque(list(map(str, input().split())))

    # 명령에 따라 커서를 왼쪽으로 옮기고(arr의 오른쪽을 narr로 옮기고)
    if commend[0] == 'L':
        if arr:
            l = arr.pop()
            narr.appendleft(l)
    # 커서를 오른쪽으로 옮기고(narr의 왼쪽을 arr로 옮기고)
    elif commend[0] == 'D':
        if narr:
            d = narr.popleft()
            arr.append(d)
    # 커서 왼쪽을 제거하고(arr의 가장 오른쪽을 제거하고)
    elif commend[0] == 'B':
        if arr:
            arr.pop()
    # 추가한다.
    elif commend[0] == 'P':
        arr.append(commend[1])

for i in arr:
    print(i, end='')
for j in narr:
    print(j, end='')