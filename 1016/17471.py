def dfs(i, n, l):
    if i == n:
        second = []
        for num in numbers:
            if num not in first:
                second.append(num)
        if [second, first[:]] not in election_ward:
            election_ward.append([first[:], second])
        return
    for j in range(l, N + 1):
        if visited[j] == 0:
            first.append(j)
            visited[j] = 1
            dfs(i + 1, n, j)
            first.pop()
            visited[j] = 0


N = int(input())
populations = [0] + list(map(int, input().split()))
# 인접 리스트를 나타내는 리스트
E_list = [[] for _ in range(N + 1)]
for i in range(1, N + 1):
    arr = list(map(int, input().split()))
    for j in range(1, arr[0] + 1):
        E_list[i].append(arr[j])

# N개 구역을 두개의 선거구로 나누는 dfs
numbers = list(range(1, N + 1))
i = 0
visited = [0] * (N + 1)
first = []
election_ward = []
for n in range(1, N // 2 + 1):
    dfs(i, n, 1)

# 두개의 선거 구역 리스트를 돌면서 각각이 연결되어 있는지 확인하고
for ward in election_ward:
    for i in ward[0]:
        can_divided = False
        if len(ward[0]) == 1:
            can_divided = True
        for j in E_list[i]:
            if j in ward[0]:
                can_divided = True
        # 연결이 하나라도 안되어 있으면
        if can_divided == False:
            break
    if can_divided == False:
        continue
    for i in ward[1]:
        can_divided = False
        for j in E_list[i]:
            if j in ward[1]:
                can_divided = True
        # 연결이 하나라도 안되어 있으면
        if can_divided == False:
            break
    if can_divided == False:
        continue

    # 두 선거구 모두 각각 연결되어 있으면
    