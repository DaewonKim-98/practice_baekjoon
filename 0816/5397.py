from collections import deque
import sys
input = sys.stdin.readline

T = int(input().strip())

for case in range(1, T + 1):
    arr = deque(list(input().strip()))
    # 커서의 왼쪽과 오른쪽 부분을 나타낼 larr, rarr
    larr = deque(list())
    rarr = deque(list())

    for word in arr:
        if word not in '<>-':
            larr.append(word)
        # 만약 larr이 있다면 커서를 왼쪽으로 하나 옮겨야 하니까 마지막을 rarr로 옮긴다.
        elif word == '<':
            if larr:
                l = larr.pop()
                rarr.appendleft(l)
        # 만약 rarr이 있다면 커서를 오른쪽으로 하나 옮겨야 하니까 마지막을 larr로 옮긴다.
        elif word == '>':
            if rarr:
                r = rarr.popleft()
                larr.append(r)
        # -면 팝으로 제거
        elif word == '-':
            if larr:
                larr.pop()

    for i in larr:
        print(i, end='')
    for j in rarr:
        print(j, end='')
    print()