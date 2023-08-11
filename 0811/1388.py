N, M = map(int, input().split())

arr = [list(input()) for _ in range(N)]

cnt = 0
# 열 탐색으로 - 개수 세기
for r in range(N):
    for c in range(M):
        # 마지막은 따로 둔다.
        if c == M - 1:
            if arr[r][c] == '-':
                cnt += 1
        else:
            # - 가 있으면 세준다.
            if arr[r][c] == '-':
                cnt += 1
            
            # 그런데 연속으로 있으면 하나씩 빼줘야 한다.
            if arr[r][c] == '-' and arr[r][c + 1] == '-':
                cnt -= 1

# 행 탐색으로 ㅣ 개수 세기
for c in range(M):
    for r in range(N):
        # 마지막은 따로 둔다.
        if r == N - 1:
            if arr[r][c] == '|':
                cnt += 1
        else:
            # - 가 있으면 세준다.
            if arr[r][c] == '|':
                cnt += 1
            # 그런데 연속으로 있으면 하나씩 빼줘야 한다.
            if arr[r][c] == '|' and arr[r + 1][c] == '|':
                cnt -= 1

print(cnt)