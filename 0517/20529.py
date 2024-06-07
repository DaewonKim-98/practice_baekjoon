from itertools import combinations

T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(str, input().split()))
    
    # 딕셔너리에 넣기
    dic = {}
    for i in range(N):
        if arr[i] in dic:
            dic[arr[i]] += 1
        else:
            dic[arr[i]] = 1
            
    # value의 max가 3을 넘으면 0
    if max(dic.values()) >= 3:
        print(0)
        continue
    # 2이하면 그냥 찾기
    cArr = combinations(arr, 3)
    minDistance = 12
    for com in cArr:
        distance = 0
        for j in range(4):
            if com[0][j] != com[1][j]:
                distance += 1
            if com[1][j] != com[2][j]:
                distance += 1
            if com[0][j] != com[2][j]:
                distance += 1
            if distance >= minDistance:
                break
        minDistance = min(minDistance, distance)
    print(minDistance)
    
    