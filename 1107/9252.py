a = list(input())
b = list(input())

# 길이가 0인 경우
set_a = set(a)
set_b = set(b)
length = False
for i in set_a:
    if i in set_b:
        length = True
        break
if length == False:
    print(0)
    exit()

a = [''] + a
b = [''] + b
# 길이가 0이 아니면 dp는 아오 문자도 출력해야 하니까 문자로 만들어야하나 문자로 ㄱㄱㄱㄱ 문자저장
dp = [[''] * len(b) for _ in range(len(a))]


for r in range(1, len(a)):
    for c in range(1, len(b)):
        # 똑같은 것을 만나면
        if a[r] == b[c]:
            dp[r][c] = dp[r - 1][c - 1] + a[r]
        # 다르다면
        else:
            if len(dp[r][c - 1]) > len(dp[r - 1][c]):
                dp[r][c] = dp[r][c - 1]
            else:
                dp[r][c] = dp[r - 1][c]


print(len(dp[len(a) - 1][len(b) - 1]))
print(dp[len(a) - 1][len(b) - 1])