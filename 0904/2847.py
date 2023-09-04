N = int(input())

scores = [int(input()) for _ in range(N)]

# 만약 자신의 앞이 자기보다 크다면 작을 때까지 -1
cnt = 0
for i in range(N -2, -1, -1):
    if scores[i] >= scores[i + 1]:
        while scores[i] >= scores[i + 1]:
            scores[i] -= 1
            cnt += 1

print(cnt)