N, K = map(int, input().split())

# 2의 제곱배들의 합을 만들어야 함
# 2진수로 표현해서 1이 K개 이하가 되면 끝
cnt = 0
while True:
    if bin(N).count('1') <= K:
        print(cnt)
        break
    N += 1
    cnt += 1