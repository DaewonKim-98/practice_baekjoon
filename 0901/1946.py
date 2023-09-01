import sys
input = sys.stdin.readline

T = int(input().strip())
for case in range(1, T + 1):
    N = int(input().strip())
    # 시간초과 때문에 서류 인덱스에 면접 성적만 추가
    arr = [0] * N
    for i in range(N):
        a, b = map(int, input().split())
        arr[a - 1] = b
    # 자신보다 등수가 높은(1등까지) 사람을 찾고 인덱스를 갱신하면서 카운트를 세주면
    # 그 사람들만 살아남는 것이므로
    cnt = 1
    min_idx = 0
    for i in range(N):
        if arr[min_idx] > arr[i]:
            min_idx = i
            cnt += 1
    print(cnt)