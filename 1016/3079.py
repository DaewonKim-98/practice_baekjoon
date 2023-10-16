N, M = map(int, input().split())
T_list = [int(input()) for _ in range(N)]

# 걸리는 시간의 최솟값을 이분탐색으로 구하기
start = 1
end = max(T_list) * M

while start <= end:
    middle = (start + end) // 2

    # 총 걸리는 시간만큼 심사를 받는 사람의 수
    people = 0
    for t in T_list:
        # 사람의 수는 총 걸리는 시간에서 각 심사대에서 걸리는 시간을 나눈 몫들을 더한 것
        people += middle // t

    # 만약 사람의 수가 M보다 많거나 같다면 총 걸리는 시간을 줄여야 하므로
    if people >= M:
        end = middle - 1

    # M보다 적다면 시간 늘리기
    else:
        start = middle + 1

print(start)