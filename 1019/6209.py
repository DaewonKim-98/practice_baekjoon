d, n, m = map(int, input().split())
arr = list(int(input()) for _ in range(n))
arr.sort()
arr = [0] + arr + [d]

# 이분탐색으로 학생들이 점프하는 최소 거리의 최댓값 구하기
start = 1
end = 1000000000

while start <= end:
    # 학생이 점프하는 거리
    middle = (start + end) // 2

    # 제거할 수 있는 돌섬의 수
    remove = 0
    # 배열을 돌면서 학생이 점프하는 거리 내에 있는 돌들 지우기
    i = 0
    j = 1
    while i < n + 1 and j < n + 2:
        # print(i, j, middle)
        # 최소 거리를 더했을 때 d를 넘어가면 그 사이에 있는 돌들 다 지우기
        if arr[i] + middle >= d:
            remove += arr[i] + middle - d
            for k in range(i + 1, n + 1):
                remove += 1
            break
        if arr[i] + middle > arr[j]:
            remove += 1
            j += 1
        else:
            i = j
            j += 1
    # print(middle, start, end)
    # 제거하는 돌들의 수가 m보다 많으면 거리를 줄여야 하므로
    if remove > m:
        end = middle - 1
    else:
        start = middle + 1

print(end)
