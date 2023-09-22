import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, D = map(int, input().split())
shortcut_list = []

for _ in range(N):
    s, e, l = map(int, input().split())
    shortcut_list.append([s, e, l])

# 지름길 시작순으로 정렬, dp를 이용해 풀기
shortcut_list.sort()
dp = [0] * (D + 1)

# dp를 돌리면서 인덱스가 지름길의 끝에 닿았을 때 판단
for i in range(1, D + 1):
    # 거리는 계속 1씩 증가하므로
    dp[i] = dp[i - 1] + 1
    # 만약 i가 지름길에 끝 점에 위치하면
    for shortcut in shortcut_list:
        if i == shortcut[1]:
            # i일 때의 거리의 최솟값은 dp[i]와 지름길의 시작 점에서 지름길의 거리를 더한 값의 최소
            dp[i] = min(dp[i], dp[shortcut[0]] + shortcut[2])

print(dp[D])