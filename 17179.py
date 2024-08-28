import sys
input = sys.stdin.readline

N, M, L = map(int, input().strip().split())
arr = [int(input().strip()) for _ in range(M)] + [L]

for _ in range(N):
    q = int(input().strip())
    # 이분탐색
    start = 0
    end = L
    
    while start <= end:
        # mid는 가장 작은 조각의 길이의 최댓값
        mid = (start + end) // 2
        cnt = 0
        piece = 0
        for length in arr:
            # 최댓값보다 크면 큰 조각이므로
            if length - piece >= mid:
                cnt += 1
                piece = length
        
        # 자른 횟수가 q보다 많으면 최댓값을 늘려야 하므로
        if cnt > q:
            start = mid + 1
        else:
            end = mid - 1
    print(end)