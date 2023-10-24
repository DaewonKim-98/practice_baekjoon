# 아아ㅏ아미아럼ㅇ닝러밇 ㅗㅁ닝럼ㄴ;ㅣㅏㅇ ㅎ매시간초과진짜 암리ㅏㅁㅇㄹ 피ㅓㅁㄴㅇ;ㅣㅏ럼ㄴㅇ ;ㅏ러
# DP로 풀어야 할듯 문제가 이따구니까 ㅁ;ㅣㄹ후니아루ㅠㅣ마어륨ㅇ;;ㅣㅡㅏㅇㄹ;ㅜ
N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]

# N이 1이거나 M이 1일 때는 무조건 1 또는 0이므로
if N == 1 or M == 1:
    for r in range(N):
        for c in range(M):
            if arr[r][c] == 1:
                print(1)
                exit()
    # 다 돌았을 때 1이 없으면 0 출력
    print(0)
    exit()

# N과 M이 1이 아닐 때
dp = [[0] * M for _ in range(N)]

# 일단 dp의 처음 행과 열은 arr과 같이 두고 시작
length = set()
dp[0] = arr[0]
length.add(max(dp[0]))
for i in range(N):
    dp[i][0] = arr[i][0]
    length.add(dp[i][0])


# 정사각형이 되기 위해서는 오른쪽 아래에서 봤을 때 왼쪽, 위, 대각선 모두가 1이어야 하고
# 0이 나오면 안되기 때문에 3개의 최솟값에서 1 더한게 오른쪽 아래가 된다면 그게 최대 정사각형의
# 한 변의 길이인가? 망ㅁㄴㅇㄴ아ㅣ러ㅜㄻㄴ;이ㅏ러;ㅣㅁ너제발무;ㅇㄴㅁ ;ㅇㄹ;ㅁ닝럼;ㄴㅇ
for r in range(1, N):
    for c in range(1, M):
        if arr[r][c] != 0:
            dp[r][c] = min(dp[r - 1][c], dp[r][c - 1], dp[r - 1][c - 1]) + 1
        length.add(dp[r][c])
# print(dp)
max_length = max(length)
print(max_length ** 2)