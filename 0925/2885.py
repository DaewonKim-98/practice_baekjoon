import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

K = int(input().strip())
# K보다 작고 가장 큰 2의 제곱수만큼 계속 빼다보면 몇 번 쪼개야할지 나올듯?
# 최대는 2의 17승이라고 생각

for i in range(24, -1, -1):
    if 2 ** i == K:
        print(2 ** i, end=' ')
        print(0)
        exit()

# 처음 가장 큰 2의 제곱수
n = 0
for i in range(24, -1, -1):
    if 2 ** i < K:
        n = i
        break
    
# 가장 작은 초콜릿의 크기는 n * 2
N = (2 ** n) * 2
# K 갱신
K = K - (2 ** n)

cnt = 0
# 초콜릿이 2의 제곱수로 나누어 떨어질 때까지 나누고 빼기
for j in range(n, -1, -1):
    if K % (2 ** j) == 0:
        cnt += 1
        break
    elif K > 2 ** j:
        K -= 2 ** j
        cnt += 1
    else:
        cnt += 1

print(N, end=' ')     
print(cnt)
