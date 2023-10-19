N, K = map(int, input().split())
arr = [0] + list(map(int, input().split()))
# 누적합으로 미리 합 구해두기
for i in range(1, N + 1):
    arr[i] = arr[i - 1] + arr[i]

# 최대한의 점수를 찾는 이분 탐색
start = 0
end = sum(arr)

while start <= end:
    middle = (start + end) // 2

    # 배열을 돌아 그룹을 묶어 합이 middle보다 크면 계속 그룹 만드기
    # 각 그룹의 합의 최소 점수가 middle이기 때문
    group = 1
    i = 0
    j = 1
    while j <= N:
        sum_score = arr[j] - arr[i]
        # print(i, j, middle, sum_score)
        # middle보다 작다면 그룹 크기 계속 늘리기
        if sum_score <= middle:
            j += 1
            continue
        # middle보다 커진다면 i 위치 변화로 새로운 그룹 만들기
        else:
            i = j
            j += 1
            group += 1

    # print(group)
    # 그룹의 수가 K보다 작다면 최대 점수가 높다는 것이므로 낮추기
    if group <= K:
        end = middle - 1
    # 아니면 최대 점수 높이기
    else:
        start = middle + 1

print(start)