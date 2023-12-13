from itertools import combinations_with_replacement

N, K = map(int, input().split())

# 막대기 K 개로 N을 만드는 중복조합 아 리스트로 하니까 메모리 터지네
# K H N = K + N - 1 C N 이므로 이걸 식을 그냥 만들어 말아 아오
result = 1
for i in range(K, K + N - 1 + 1):
    result *= i

for j in range(1, N + 1):
    result //= j
    
print(result % 1000000000)