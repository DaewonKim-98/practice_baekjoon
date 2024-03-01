from itertools import combinations

N, M = map(int, input().split())

arr = [set() for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    arr[a].add(b)
    arr[b].add(a)

# 조합에서 섞어먹으면 안되는 것들이 있으면 컷
lst = list(combinations(list(range(1, N + 1)), 3))

cnt = 0
# 전체 조합을 돌면서
for com in lst:
    # 조합을 돌면서
    for i in com:
        isGood = True
        # 조합안에 있는 다른 요소가 섞어먹어도 안되는 것이면
        for j in com:
            if j in arr[i]:
                isGood = False
                break
        
        # 섞어먹어도 안되는 것이 있으면
        if isGood == False:
            break
    
    # 전체가 break되지 않고 잘 벗어났으면 섞어먹어도 되는 것이므로
    else:
        cnt += 1
        
print(cnt)
            