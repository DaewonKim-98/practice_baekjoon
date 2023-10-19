N, M = map(int, input().split())
arr = [0] + list(map(int, input().split()))
# 누적합
for i in range(N):
    arr[i + 1] = arr[i] + arr[i + 1]
    
# print(arr)
# 최댓값을 찾는 이분탐색으로 그룹 구하기
start = arr[1]
end = arr[-1]
while start <= end:
    # 각 그룹의 최댓값
    middle = (start + end) // 2

    # 그룹의 개수
    groups = 0
    i = 0
    j = N
    group_list = []
    while i < N:
        # 그룹의 합이 어떤 최댓값보다 크면 계속 합을 줄이기
        if arr[j] - arr[i] > middle:
            j -= 1
            # 이렇게 되었다는건 하나짜리가 어떤 최댓값보다 크다는 것이므로
            if i == j:
                groups += M + 1
                break
        else:
            groups += 1
            i = j
            j = N
    
    # 그룹의 개수가 M보다 작다면 최댓값을 줄여야하므로
    if groups <= M:
        end = middle - 1
    else:
        start = middle + 1

# 그룹으로 나눴을 때 합이 N보다 작으면 마지막 부분은 되지 않았다는 것이므로 
# 최솟값을 찾았으므로 그룹을 나누기
i = 0
j = 1
num_groups = []
while j < N + 1:
    if arr[j] - arr[i] <= start:
        j += 1
            
    else:
        # print(i, j)
        num_groups.append(j - i - 1)
        i = j - 1
        j += 1 

# 다 돌았을 때 그룹의 개수가 N 작으면 마지막 것들은 들어가지 않은 것이므로
if sum(num_groups) < N:
    num_groups.append(N - sum(num_groups))

# 그룹이 나누어 졌을 때 그룹의 개수가 M개보다 작으면 그 안의 그룹에서 또 나눠주어 총 그룹의 개수가
# M이 될 때까지 하기
while len(num_groups) < M:
    for i in range(len(num_groups)):
        if num_groups[i] > 1:
            num_groups[i] -= 1
            num_groups.insert(i, 1)
            if len(num_groups) == M:
                break
    if len(num_groups) == M:
            break

print(start)
for i in num_groups:
    print(i, end=' ')
    