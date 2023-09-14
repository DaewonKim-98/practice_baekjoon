import sys
sys.stdin = open('input.txt')
from collections import deque
input = sys.stdin.readline

N = int(input().strip())
# 처음에 0을 두고 시작
arr = deque([0])
cnt = 1

for i in range(N):
    x = int(input().strip())

    # x가 0일 때
    if x == 0:
        # 0만 있으면 0출력
        if cnt == 1:
            print(0)
        elif cnt > 1:
            # 0을 제거해주고 최솟값 출력 후 다시 0 채우기
            arr.popleft()
            print(arr.popleft())
            arr.appendleft(0)
            cnt -= 1
            i = 1
            # 남은 노드의 개수가 2개 이상이면
            if cnt > 2:
                arr.popleft()
                arr.appendleft(arr.pop())
                arr.appendleft(0)
                while i < cnt:
                    # 자식 노드가 없으면
                    if i * 2 >= cnt:
                        break
                    # 자식 노드가 하나면
                    elif i * 2 + 1 >= cnt:
                        if arr[i] > arr[i * 2]:
                            arr[i], arr[i * 2] = arr[i * 2], arr[i]
                        break
                    # 자식 노드가 모두 있으면
                    else:
                        if arr[i * 2] < arr[i * 2 + 1]:
                            if arr[i] > arr[i * 2]:
                                arr[i], arr[i * 2] = arr[i * 2], arr[i]
                                i *= 2
                            else:
                                break
                        else:
                            if arr[i] > arr[i * 2 + 1]:
                                arr[i], arr[i * 2 + 1] = arr[i * 2 + 1], arr[i]
                                i = i * 2 + 1
                            else:
                                break

    # x가 0이 아닐 때
    else:
        if cnt == 1:
            arr.append(x)
            cnt += 1
        elif cnt > 1:
            arr.append(x)
            cnt += 1
            # 부모 노드와 비교해서 루트로 올리기
            i = cnt - 1
            while i > 1:
                if arr[i] < arr[i // 2]:
                    arr[i], arr[i // 2] = arr[i // 2], arr[i]
                    i //= 2
                else:
                    break