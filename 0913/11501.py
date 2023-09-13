import sys
input = sys.stdin.readline

T = int(input().strip())
for case in range(1, T + 1):
    N = int(input().strip())
    arr = list(map(int, input().split()))

    # 주가가 최대일 때까지 샀다가 팔면 가장 이익이므로 
    profits = 0
    while True:
        # arr이 하나 이하면 필요 없으므로
        if len(arr) <= 1:
            break
        max_idx = arr.index(max(arr))
        buy = 0
        # 이익 갱신
        for i in range(max_idx):
            buy += arr[i]
        profits += arr[max_idx] * max_idx - buy

        # arr 갱신
        arr = arr[max_idx + 1:]

    print(profits)