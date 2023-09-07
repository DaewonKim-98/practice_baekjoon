N = int(input())

if N == 1 or N == 2 or N == 4:
    print(0)
    exit()

cnt = 0
# i가 가장 높은 수라고 할 때 i의 범위는 이렇게
for i in range(N // 3, N // 2 + 1):
    # j는 N에서 i를 뺀 것에서 2를 나눈 것부터 시작해서 줄어들고
    for j in range((N - i) // 2, 0, -1):
        # i 와 j 를 제외한 나머지가 i보다 커진다면 말이안되므로 break
        if N - i - j > i or i * 2 == N:
            break
        cnt += 1

print(cnt)