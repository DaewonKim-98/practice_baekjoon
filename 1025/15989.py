T = int(input())
for tc in range(T):
    n = int(input())
    answer = 0

    while n >= 0:
        answer += n // 2 + 1
        n -= 3
    print(answer)