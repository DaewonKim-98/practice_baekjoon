import sys
input = sys.stdin.readline

T = int(input().strip())

for _ in range(T):
    N, K = map(int, input().strip().split())
    arr = list(map(int, input().strip().split()))
    arr.sort()
    # 끝과 끝에서 시작해서 K와 가까운거 찾기
    i, j = 0, N - 1
    cnt = 0
    closeK = 300000000
    while i < j:
        sumInt = arr[i] + arr[j]
        # 합이 K보다 작으면
        if sumInt < K:
            i += 1
            # 차가 최소보다 작으면 갱신
            if K - sumInt < closeK:
                cnt = 1
                closeK = K - sumInt
            # 차가 최소와 같으면 +
            elif K - sumInt == closeK:
                cnt += 1
        # 합이 K보다 크면
        elif sumInt > K:
            j -= 1
            if sumInt - K < closeK:
                cnt = 1
                closeK = sumInt - K
            elif sumInt - K == closeK:
                cnt += 1
        # 합이 K와 같으면
        else:
            i += 1
            if closeK != 0:
                cnt = 1
                closeK = 0
            else:
                cnt += 1
    print(cnt)