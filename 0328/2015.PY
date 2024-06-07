N, K= map(int, input().split())
arr = list(map(int, input().split()))
# 누적합
arrSum = arr.copy()
for i in range(1, N):
    arrSum[i] += arrSum[i - 1]

# 누적합에 따라 인덱스 dic에 저장
dic = {}
dic[0] = 1

cnt = 0
# K를 뺀게 앞에 있으면 개수세고 걍 계속 저장?
for i in range(N):
    if arrSum[i] - K in dic:
        cnt += dic[arrSum[i] - K]
        
    if arrSum[i] in dic:
        dic[arrSum[i]] += 1
    else:
        dic[arrSum[i]] = 1

# 마지막엔 누적합이 K인 것 찾기 아 이거네 개쉽넹마ㅣㅇㄴㅁㄹ미ㅏㄴ후망ㄹ훔
print(cnt)