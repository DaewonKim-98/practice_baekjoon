N, K = map(int, input().split())
share = list(map(int, input().split()))
team = list(map(int, input().split()))

if N == 0 or N == K:
    print(0)
    exit()

# share에서 min, max 찾고 team에서 그것과 매칭 되는
# 가장 큰 것들 K개 없애기
minValue = min(share)
maxValue = max(share)

# K개 돌면서 삭제
for _ in range(K):
    maxScore = -100000000
    index = 0
    for i in range(N):
        # 더 크면 갱신
        if minValue * team[i] > maxScore:
            maxScore = minValue * team[i]
            index = i
        if maxValue * team[i] > maxScore:
            maxScore = maxValue * team[i]
            index = i
            
    # 갱신 되었으면 삭제
    team.remove(team[index])
    N -= 1
    
# K개를 다 삭제했으면 최대 점수 다시 찾기
maxScore = -100000000
for i in range(N):
    # 더 크면 갱신
    if minValue * team[i] > maxScore:
        maxScore = minValue * team[i]
    if maxValue * team[i] > maxScore:
        maxScore = maxValue * team[i]
   
print(maxScore)
