N, K, B = map(int, input().split())

# 횡단보도
block = [0] * N
# 고장난 것 추가
for _ in range(B):
    i = int(input())
    block[i - 1] = 1
    
# 범위 안에 고장난 것이 있으면 마지막 인덱스에 그 개수 추가
fix_block = [0] * N
fix_block[0] = block[0]
for i in range(1, N):
    if block[i] == 1:
        fix_block[i] = fix_block[i - 1] + 1
    else:
        fix_block[i] = fix_block[i - 1]

# 최소 수리 신호등 갱신
min_fix = K
for j in range(N - K):
    if min_fix > fix_block[j + K] - fix_block[j]:
        min_fix = fix_block[j + K] - fix_block[j]
        
print(min_fix)
