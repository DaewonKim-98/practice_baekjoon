N, K = map(int, input().split())

# 앞에서부터 빼주기
i = 1
while True:
    # i자리 수보다 K가 크면 계속
    if K - i * (10 ** i - 10 ** (i - 1)) > 0:
        K -= i * (10 ** i - 10 ** (i - 1))
        i += 1
    else:
        break

# 원래의 K는 i자리 수에서 K번째가 되므로
cnt = 0
while True:
    # cnt번째 수보다 크면 계속
    if K - i > 0:
        K -= i
        cnt += 1
    else:
        break

# 원래의 K는 i자리의 cnt번째에서 남은 K만큼 더 간 곳
number = 10 ** (i - 1) + cnt
if N < number:
    print(-1)
else:
    print(str(number)[K - 1])