N = int(input())
arr = list(map(int, input().split()))

# 딕셔너리에 저장하면서 ㄱㄱ
numbersDic = {}
numbersDic[0] = [arr[0]]
dp = [1] * N

for i in range(1, N):
    numbersDic[i] = [arr[i]]
    for j in range(i):
        # 증가하면
        if arr[j] < arr[i]:
            # 더 크면 바꾸기
            if dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                numbersDic[i] = numbersDic[j] + [arr[i]]

maxIndex = dp.index(max(dp))
                
print(dp[maxIndex])
for j in numbersDic[maxIndex]:
    print(j, end=' ')
