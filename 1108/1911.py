N, L = map(int, input().split())

# 웅덩이
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort()

# 처음부터 돌면서 널빤지를 추가하고 추가한 널빤지에 웅덩이가 있으면 계속 널빤지 추가
# 웅덩이 없으면 다시 웅덩이를 만났을 때 널빤지 추가
# 이건 무조건 맞다 ㄹㅇ 지렸다
i = 0
cnt = 0
# 널빤지 위치
nul = 0
while i < N:
    # 널빤지가 웅덩이의 시작을 덮고 있지 않으면
    if nul < arr[i][0]:
        # 널빤지는 웅덩이의 시작점으로
        nul = arr[i][0]
        # 웅덩이를 덮을 때까지 널빤지 추가
        while nul < arr[i][1]:
            nul += L
            cnt += 1
        i += 1
    # 널빤지가 웅덩이의 시작을 덮고 있으면
    else:
        # 웅덩이를 또 모두 덮을 때까지 널빤지 추가
        while nul < arr[i][1]:
            nul += L
            cnt += 1
        i += 1
print(cnt)