N, M = map(int, input().split())

arr = []
for i in range(N):
    row = list(map(str, input()))
    # 2차원 리스트 만들기
    arr = arr + [row]

# 행의 경비원을 r_guard로 둔다.
r_guard = 0
for r in range(N):
    cnt = 0
    # 행에서 경비원이 있으면 cnt에 1 추가
    for c in range(M):
        if arr[r][c] == 'X':
            cnt += 1
    # cnt가 0이라는 것은 경비원이 없다는 것이므로 r_guard에 1 추가
    if cnt == 0:
        r_guard += 1

# 열 경비원도 마찬가지로 찾는다.
c_guard = 0
for c in range(M):
    cnt = 0
    for r in range(N):
        if arr[r][c] == 'X':
            cnt += 1
    if cnt == 0:
        c_guard += 1

# 경비원의 수의 최솟값은 행과 열에서 큰 값들을 출력한 것
if r_guard <= c_guard:
    print(c_guard)
else:
    print(r_guard)