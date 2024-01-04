N = int(input())
arr = list(map(int ,input().split()))

# 거짓말한 사람이 0명이면 모두 진실 1명이면 2명 이상, 3명 이상,,,거짓말을 하는 사람이 0
# 거짓말한 사람이 1명이면 2명 이상, 3명 이상,,,이 거짓말을 하고 있는 사람 + 
# + 0명 이하가 거짓말을 하고 있는 사람이 1명
# 거짓말한 사람이 2명이면 3명 이상, 4명 이상 거짓말을 하고 있다는 사람 +
# 0명 이하, 1명 이하가 거짓말을 하고 있다고 말한 사람이 총 2명

# 0명 이하, 1명 이하, ,,, 를 나타내는 사람들의 수를 나타내는 리스트
down = [0] * (N + 1)
# 1명 이상, 2명 이상 ,,, 을 나타내는 사람들의 수를 나타내는 리스트
up = [0] * (N + 1)
for i in arr:
    if i <= 0:
        down[-i] += 1
    else:
        up[i] += 1
        
# 누적합
for i in range(1, N + 1):
    down[i] += down[i - 1]
    up[i] += up[i - 1]
    
# print(up)
# print(down)

lying = []
# 1~명 이상 거짓말을 하고 있는 사람이 없으면
if up[N] == 0:
    lying.append('0')
# 거짓말을 하고 있는 사람이 k명이면 그 것에 대해 판별
for k in range(1, N + 1):
    if up[N] - up[k] + down[k - 1] == k:
        lying.append(str(k))
         
print(len(lying))
print(' '.join(lying))