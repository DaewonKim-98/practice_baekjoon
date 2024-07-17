N = int(input())
arr = [0] * 2 + list(map(int, input().split()))

# 가중치 주기
sumArr = arr.copy()
for i in range(len(arr)):
    sumArr[i] += sumArr[i // 2]
    
# 최대 가중치
maxArr = max(sumArr)

# dfs로 아래 애들부터 최대 가중치를 만들기 위해 더해주기
for i in range(2, len(arr)):
    dfs(i)