N, M = map(int, input().split())
arr = [0] + list(map(int, input().split()))

compliment = {}
for i in range(1, N + 1):
    compliment[i] = 0

# 아 어차피 직속 상사의 번호는 무조건 내보다 작으니까 걍 dfs 필요 없네
# 일단 걍 칭찬
for _ in range(M):
    i, w = map(int, input().split())
    compliment[i] += w

# 이후 직속 상사들의 칭찬 더해줘라
for i in range(2, N + 1):
    compliment[i] += compliment[arr[i]]
    
    
for k, v in compliment.items():
    print(v, end=' ')