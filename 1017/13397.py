N, M = map(int, input().split())
arr = list(map(int, input().split()))

# 구간의 점수를 이분탐색으로 찾으면서 구간 점수의 최댓값의 최솟값 찾기
start = 0
end = 10000

while start <= end:
    middle = (start + end) // 2

    # 구간의 개수
    cnt = 0
    # 구간의 개수는 구간에서 최댓값과 최솟값의 차가 middle보다 작은 것들의 개수와 같으므로
    i = 0
    j = 1
    while j <= N:
        # print(i, middle)
        # 구간의 최댓값과 최솟값의 차가 middle보다 작거나 같다면 그 구간을 계속 늘려도 되므로
        if max(arr[i:j]) - min(arr[i:j]) <= middle:
            j += 1
            continue
        else:
            i = j - 1
            cnt += 1

    # 구간의 개수 1 더해주기
    cnt += 1
    # print(cnt) 
    # print(start, end)
    # 만약 구간의 개수가 M보다 크다면 최댓값을 늘려야 하므로
    if M < cnt:
        start = middle + 1
    # 구간의 개수가 M보다 작거나 같다면 최댓값을 줄여야 하므로
    else:
        end = middle - 1

print(start)