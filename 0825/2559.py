import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

# 연속적인 숫자들은 겹치는 부분이 있고 그 부분들을 빼고 계산하면 합을
# 쉽게 구할 수 있다.
# 합 리스트
sum_list = [sum(arr[:K])]
for i in range(N - K):
    sum_list.append(sum_list[i] - arr[i] + arr[i + K])
    
print(max(sum_list))

